import subprocess

from .poll import check_notifications
from ..popup import VolumeSlider
from ..status import NotificationStatus


# Notifications

def toggle_notification_history(qtile):
    _, paused = check_notifications()
    history = int(subprocess.check_output(["dunstctl", "count", "history"], text=True).strip())

    if history:
        for notification in range(history):
            qtile.spawn("dunstctl history-pop")
        _update_notification_widget(qtile, paused, 0)
    else:
        displayed = int(
            subprocess.check_output(["dunstctl", "count", "displayed"], text=True).strip()
        )
        if displayed:
            qtile.spawn("dunstctl close-all")
        _update_notification_widget(qtile, paused, displayed)


def pause_notifications(qtile):
    count, paused = check_notifications()
    qtile.spawn("dunstctl set-paused toggle")
    _update_notification_widget(qtile, not paused, count)


def clear_notifications(qtile):
    _, paused = check_notifications()
    qtile.spawn("dunstctl history-clear")
    _update_notification_widget(qtile, paused, 0)


def _update_notification_widget(qtile, paused, count):
    # Workaround for widget update delay
    widget = qtile.widgets_map["notifications"]

    if paused:
        widget.update(NotificationStatus.PAUSED.value)
    elif count:
        widget.update(NotificationStatus.NEW.value)
    else:
        widget.update(NotificationStatus.CLEAR.value)


# Actions/Shortcuts

volume_slider = VolumeSlider()

def volume_change(qtile, action):
    hidden = volume_slider.hidden

    # Only refresh actual volume level when displaying after being hidden; prevents stuttering
    if hidden:
        volume_change.volume, volume_change.mute = _get_volume_results()

    value, decrease = action.value

    volume_change.volume += (-value if decrease else value) / 100

    if hidden:
        volume_slider._configure(qtile)
        volume_slider.show()
    volume_slider.update(volume_change.volume)

    if volume_change.mute:
        qtile.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ 0")
    qtile.spawn(
        "wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ {}%{}"
        .format(value, "-" if decrease else "+")
    )


def _get_volume_results():
    results = subprocess.check_output(
        ["wpctl", "get-volume", "@DEFAULT_AUDIO_SINK@"], text=True
    ).strip().split(" ")

    volume = float(results[1])
    mute = len(results) == 3 and results[2] == "[MUTED]"

    return volume, mute

