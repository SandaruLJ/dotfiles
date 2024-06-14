import subprocess

from .poll import check_notifications
from ..status import NotificationStatus


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

