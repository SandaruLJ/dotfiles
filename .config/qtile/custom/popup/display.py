from . import GenericPopup
from ..status import BrightnessStatus


class BrightnessSlider(GenericPopup):
    def update(self, brightness):
        if brightness <= 0.3:
            icon = BrightnessStatus.LOW.value
        if brightness < 0.8:
            icon = BrightnessStatus.MEDIUM.value
        else:
            icon = BrightnessStatus.HIGH.value

        self.update_controls(icon=icon, value=brightness)

