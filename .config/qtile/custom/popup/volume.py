from . import GenericPopup
from ..status import MicStatus, VolumeStatus


class VolumeSlider(GenericPopup):
    def update(self, volume):
        if volume <= 0:
            icon = VolumeStatus.MUTE.value
        elif volume <= 0.3:
            icon = VolumeStatus.LOW.value
        elif volume < 0.8:
            icon = VolumeStatus.MEDIUM.value
        else:
            icon = VolumeStatus.HIGH.value

        self.update_controls(icon=icon, value=volume)


class MicSlider(GenericPopup):
    def update(self, volume):
        if volume <= 0:
            icon = MicStatus.MUTE.value
        else:
            icon = MicStatus.NORMAL.value

        self.update_controls(icon=icon, value=volume)

