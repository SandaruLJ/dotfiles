from enum import Enum

class NotificationStatus(Enum):
    CLEAR = "󰂚"
    NEW = "󱅫"
    PAUSED = "󰂛"


class VolumeStatus(Enum):
    MUTE = "󰝟"
    LOW = "󰕿"
    MEDIUM = "󰖀"
    HIGH = "󰕾"


class MicStatus(Enum):
    NORMAL = "󰍬"
    MUTE = "󰍭"

