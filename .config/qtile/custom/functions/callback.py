import subprocess


def toggle_notification_history(qtile):
    proc = subprocess.run(["dunstctl", "count", "displayed"], capture_output=True, text=True)

    try:
        displayed = bool(int(proc.stdout.strip()))
    except:
        displayed = False

    if displayed:
        cmd = "dunstctl close-all"
    else:
        cmd = "dunstctl history-pop"

    qtile.spawn(cmd)

