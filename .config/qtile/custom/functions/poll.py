import subprocess

from ..status import NotificationStatus


def get_notification_status():
    count, paused = check_notifications()

    if paused:
        return NotificationStatus.PAUSED.value
    if count:
        return NotificationStatus.NEW.value
    return NotificationStatus.CLEAR.value


def check_notifications():
    count = subprocess.check_output(["dunstctl", "count", "history"], text=True).strip()
    paused = subprocess.check_output(["dunstctl", "is-paused"], text=True).strip()

    return int(count), paused == "true"

