from copy import copy

from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupSlider, PopupText


DEFAULT_WIDTH=250
DEFAULT_HEIGHT=40
DEFAULT_CONTROLS = [
    PopupText(
        name="icon",
        pos_x=0.01,
        pos_y=0.15,
        height=0.8,
        width=0.15,
        v_align="middle",
        h_align="center",
        fontsize=20,
        ),
    PopupSlider(
        name="value",
        pos_x=0.195,
        pos_y=0.1,
        width=0.75,
        height=0.8,
        colour_below="00ffff",
        bar_border_size=2,
        bar_border_margin=1,
        bar_size=5,
        marker_size=0,
        end_margin=0,
        ),
]

DEFAULT_SHOW_ARGS = {
    "hide_on_timeout": 1,
    "relative_to": 2,
    "y": 16,
}


class GenericPopup(PopupRelativeLayout):
    def __init__(self, height=DEFAULT_HEIGHT, width=DEFAULT_WIDTH, controls=DEFAULT_CONTROLS):
        super().__init__(width=width, height=height, controls=controls)
        self._killed = True

    def _configure(self, qtile):
        super()._configure(qtile)
        self._killed = False

    @property
    def hidden(self):
        return self._killed

    def show(self, **kwargs):
        show_args = copy(DEFAULT_SHOW_ARGS)
        show_args.update(kwargs)
        super().show(**show_args)

    def update(self):
        """The implementation should call self.update_controls() method"""
        raise NotImplementedError

