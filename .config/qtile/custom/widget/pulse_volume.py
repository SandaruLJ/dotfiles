from libqtile.widget.pulse_volume import PulseVolume as QPulseVolume
from libqtile.widget.pulse_volume import pulse


class PulseVolume(QPulseVolume):
    def __init__(self, **config):
        self._set_mouse_callbacks(config)
        super().__init__(**config)
        self.sink = None
        self.show_sink_info = False
        self.sink_info_text = ""

    def _set_mouse_callbacks(self, config):
        default_callbacks = {"Button1": self.toggle_sink_info}
        if "mouse_callbacks" not in config:
            config.update(mouse_callbacks=default_callbacks)

    def draw(self):
        # Remove background
        self.drawer.clear(self.background or self.bar.background)

        # Draw parent widget (text/emoji/icon indicator)
        super().draw()

        # Define offset for sink info text
        offset = super().calculate_length()

        if self.show_sink_info and self.sink_info_text:
            text = self.sink_info_text

            # Create a text box
            layout = self.drawer.textlayout(
                text, self.foreground, self.font, self.fontsize, None, wrap=False
            )
            # Center vertically
            y_offset = (self.bar.height - layout.height) / 2
            # Set layout as wide as text
            layout.width = self._max_text_length(self.sink_info_text)

            # Draw and increase the offset
            layout.draw(offset, y_offset)

        # Redraw the bar
        self.drawer.draw(offsetx=self.offset, offsety=self.offsety, width=self.length)

    def toggle_sink_info(self):
        self.show_sink_info = not self.show_sink_info
        self.bar.draw()

    def get_vals(self, vol, muted):
        # Override subscribed method to pulse so sink info can be updated
        self.sink = pulse.default_sink
        self._update_sink_info_text(vol)
        super().get_vals(vol, muted)

    def _update_sink_info_text(self, volume):
        if not self.sink:
            return

        sink = self.sink.description
        active_port = self.sink.port_active.description
        self.sink_info_text = f"{active_port} - {sink} ({volume}%)"

    def calculate_length(self):
        parent = super().calculate_length()
        if not (self.show_sink_info and self.sink_info_text):
            return parent

        # Add length of sink info text to that of parent widget
        sink_info_text = self._max_text_length(self.sink_info_text)
        return parent + sink_info_text + self.actual_padding

    def _max_text_length(self, text):
        return self.drawer.max_layout_size([text], self.font, self.fontsize)[0]

