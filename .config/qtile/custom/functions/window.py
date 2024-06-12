def move_to_next_screen(qtile):
    _move_to_screen(qtile, 1)


def move_to_prev_screen(qtile):
    _move_to_screen(qtile, -1)


def _move_to_screen(qtile, direction=1):
    other_screen = (qtile.screens.index(qtile.current_screen) + direction) % len(qtile.screens)
    other_group = None

    for group in qtile.get_groups().values():
        if group["screen"] == other_screen:
            other_group = group["name"]
            break

    if other_group:
        qtile.move_to_group(other_group)
        qtile.to_screen(other_screen)

