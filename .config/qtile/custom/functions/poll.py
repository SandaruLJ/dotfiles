import subprocess


def check_notifications():
    proc_paused = subprocess.run(["dunstctl", "is-paused"], capture_output=True, text=True)
    proc_count = subprocess.run(["dunstctl", "count", "history"], capture_output=True, text=True)

    try:
        paused = proc_paused.stdout.strip() == "true"
        count = int(proc_count.stdout.strip())
    except:
        paused = False
        count = 0

    if paused:
        return "󰂛"
    if count:
        return "󱅫"
    return "󰂚"

