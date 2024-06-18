import asyncio

import pulsectl_asyncio
from libqtile.widget.pulse_volume import PulseConnection as QPulseConnection
from libqtile.widget.volume import Volume
from libqtile.utils import logger

from custom.widget.pulse_volume import PulseVolume


lock = asyncio.Lock()


class PulseConnection(QPulseConnection):
    def __init__(self):
        super().__init__()
        self.default_source = None
        self.default_source_name = None

    async def _configure(self):
        async with lock:
            if self.configured:
                return

            self.pulse = pulsectl_asyncio.PulseAsync("qtile-pulse-mic")
            await self._check_pulse_connection()

            self.configured = True

    async def _event_listener(self):
        async for event in self.pulse.subscribe_events("source", "server"):
            if event.facility == "source":
                await self.get_source_info()
            elif event.facility == "server":
                await self.get_server_info()

    async def get_server_info(self):
        info = await self.pulse.server_info()
        self.default_source_name = info.default_source_name
        await self.get_source_info()

    async def get_source_info(self):
        self.default_source = await self.pulse.source_default_get()
        if not self.default_source:
            logger.warning("Could not get info for default source")
            self.default_source = None
            return

        self.update_clients()

    def get_mic_status(self):
        if not self.pulse.connected:
            return None, None, None

        if self.default_source:
            state = self.default_source.state._value
            mute = self.default_source.mute
            base = self.default_source.base_volume
            if not base:
                return state, mute, -1
            current = self.default_source.volume.value_flat
            return state, mute, round(current * 10 / base)
        return "", 0, -1

    def update_clients(self):
        for callback in self.callbacks:
            callback(*self.get_mic_status())


class PulseMic(PulseVolume):
    def __init__(self, active_icon="󰍬", muted_icon="󰍭", **config):
        self._set_mouse_callbacks(config)
        super().__init__(**config)

        self.pulse = None
        self.source = None
        self.active_icon = active_icon
        self.muted_icon = muted_icon
        self.active = False
        self.muted = False
        self.configured = False

        if not hasattr(self, "icon_color"):
            self.icon_color = self.foreground

    def _configure(self, qtile, bar):
        Volume._configure(self, qtile, bar)
        self.pulse = PulseConnection()
        self.pulse.subscribe(self.get_vals)
        self.configured = True

    def _set_mouse_callbacks(self, config):
        super()._set_mouse_callbacks(config)

    def draw(self):
        self._update_drawer()

        original_foreground = self.foreground
        if not self.show_device_info:
            self.foreground = self.icon_color

        super().draw()

        self.foreground = original_foreground

    def _update_drawer(self):
        if self.active:
            self.text = self.muted_icon if self.muted else self.active_icon
        else:
            if self.configured and self.pulse.pulse.connected:
                self.text = ""
            else:
                self.text = self.error

    def get_vals(self, state, muted, volume):
        if not self.configured:
            return

        prev_state = self.active

        self.source = self.pulse.default_source
        self.active = state == "running"
        self.muted = muted

        self._update_device_info(volume, prev_state != self.active)

    def _update_device_info(self, _, state_changed):
        if not self.source:
            return

        prev_length = len(self.device_info_text)

        source = self.source.description
        active_port = self.source.port_active.description
        self.device_info_text = f"{active_port} - {source}"

        self.draw()

        # Redraw bar if text length or active status changes
        if prev_length != len(self.device_info_text) or state_changed:
            self.bar.draw()

    def finalize(self):
        self.pulse.unsubscribe(self.get_vals)
        Volume.finalize(self)

