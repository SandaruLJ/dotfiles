from libqtile.widget.base import _TextBox
from libqtile.widget.pulse_volume import PulseVolume as QPulseVolume
from libqtile.widget.pulse_volume import pulse


class PulseVolume(QPulseVolume):
    def __init__(self, text_length=36, device_info_timeout=5, error="󱈸", **config):
        self._set_mouse_callbacks(config)
        super().__init__(**config)

        self.sink = None
        self.show_device_info = False
        self.device_info_text = ""
        self.hide_timer = None
        self.error = error
        self.text_length = text_length
        self.device_info_timeout = device_info_timeout
        self.text = self.error  # Show error until connected to pulse server

    def _set_mouse_callbacks(self, config):
        default_callbacks = {"Button1": self.toggle_device_info}
        if "mouse_callbacks" not in config:
            config.update(mouse_callbacks=default_callbacks)

    def draw(self):
        # Remove background
        self.drawer.clear(self.background or self.bar.background)

        # Draw parent widget (text/emoji/icon indicator)
        super().draw()

        # Define offset for device info text
        offset = super().calculate_length()

        if self.show_device_info and self.device_info_text:
            text = self.device_info_text

            # Create a text box
            layout = self.drawer.textlayout(
                text, self.foreground, self.font, self.fontsize, None, wrap=False
            )
            # Center vertically
            y_offset = (self.bar.height - layout.height) / 2
            # Set width, accounting for text length limit
            layout.width = self._max_text_length(text[:self.text_length])

            # Draw the text box
            layout.draw(offset, y_offset)

        # Redraw the bar
        self.drawer.draw(offsetx=self.offset, offsety=self.offsety, width=self.length)

    def _update_drawer(self):
        super()._update_drawer()
        if pulse.pulse and not pulse.pulse.connected:
            self.text = self.error

    def toggle_device_info(self):
        self.show_device_info = not self.show_device_info
        if self.show_device_info:
            self.hide_timer = self.timeout_add(self.device_info_timeout, self.hide_device_info)
        else:
            self.hide_timer and self.hide_timer.cancel()
        self.bar.draw()

    def hide_device_info(self):
        self.show_device_info = False
        self.bar.draw()

    def get_vals(self, vol, muted):
        # Override subscribed method to pulse so device info can be updated
        self.sink = pulse.default_sink
        self._update_device_info_text(vol)
        super().get_vals(vol, muted)

    def _update_device_info_text(self, volume):
        if not self.sink:
            return

        prev_length = len(self.device_info_text)

        sink = self.sink.description
        active_port = self.sink.port_active.description
        self.device_info_text = f"({volume}%) {active_port} - {sink}"

        # Redraw bar if text length changes
        if prev_length != len(self.device_info_text):
            self.bar.draw()

    def calculate_length(self):
        parent = super().calculate_length()
        if not (self.show_device_info and self.device_info_text):
            return parent

        # Add length of device info text to that of parent widget
        device_info_text = self._max_text_length(self.device_info_text[:self.text_length])
        return parent + device_info_text + self.actual_padding

    def _max_text_length(self, text):
        return self.drawer.max_layout_size([text], self.font, self.fontsize)[0]

    def button_press(self, x, y, button):
        _TextBox.button_press(self, x, y, button)

