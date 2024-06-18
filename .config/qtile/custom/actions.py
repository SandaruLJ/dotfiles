from enum import Enum


class VolumeAction(Enum):
    # action = value, decrease
    UP = 1, False
    DOWN = 1, True
    UP_HIGHER_STEPS = 5, False
    DOWN_HIGHER_STEPS = 5, True

