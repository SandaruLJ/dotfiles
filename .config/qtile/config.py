# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile import bar, hook, layout, qtile, widget
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget as extra_widget, hook as extra_hook

from custom import widget as custom_widget
from custom.functions import window


mod = "mod4"
terminal = guess_terminal()
file_manager = "thunar"
launcher = "rofi -show drun"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod, "control"],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Open application launcher
    Key([mod], "e", lazy.spawn("rofi -show drun"), desc="Open application launcher"),
    Key([mod], "w", lazy.spawn("rofi -show window"), desc="Open window selector"),
    # Switch monitors
    Key([mod], "period", lazy.next_screen(), desc="Switch to next monitor"),
    Key([mod], "comma", lazy.next_screen(), desc="Switch to previous monitor"),
    Key(
        [mod, "shift"],
        "period",
        lazy.function(window.move_to_next_screen),
        desc="Move window to next monitor"
    ),
    Key(
        [mod, "shift"],
        "comma",
        lazy.function(window.move_to_prev_screen),
        desc="Move window to previous monitor"
    ),
    # Volume control
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ 1%+"),
        desc="Increase volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ 1%-"),
        desc="Decrease volume",
    ),
    Key(
        ["shift"],
        "XF86AudioRaiseVolume",
        lazy.spawn("wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ 5%+"),
        desc="Increase volume (higher steps)"
    ),
    Key(
        ["shift"],
        "XF86AudioLowerVolume",
        lazy.spawn("wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ 5%-"),
        desc="Decrease volume (higher steps)"
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"),
        desc="Toggle mute"
    ),
    # Mic control
    Key(
        [],
        "XF86AudioMicMute",
        lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle"),
        desc="Toggle mic mute"
    ),
    # Playback control
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), "Play/pause media"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), "Next track"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), "Previous track"),
    # Brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%"), desc="Increase brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-"), desc="Increase brightness"),
    # Lock screen
    Key(
        ["mod1", "control"],
        "l",
        lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/lock_screen.sh")),
        desc="Lock screen"
    ),
    # Change wallpaper
    Key(
        [mod, "control"],
        "w",
        lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/wallpaper_cycle.sh --rand")),
        desc="Change to a random wallpaper"
    ),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


# groups = [Group(i) for i in "123456789"]

groups = [
    Group(name="a", label=""),
    Group(name="s", label=""),
    Group(name="d", label=""),
    Group(name="f", label=""),
    Group(name="u", label=""),
    Group(name="i", label=""),
    Group(name="o", label=""),
    Group(name="p", label=""),
]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# Dropdown windows
groups.append(
    ScratchPad("scratchpad", [
        DropDown("dd_term", terminal),
    ]),
)

keys.extend([
    Key(
        [mod, "control"],
        "Return",
        lazy.group["scratchpad"].dropdown_toggle("dd_term"),
        desc="Open terminal as a dropdown window",
    ),
])

# Colours
colors = {
    "bg": "#181818",
    "accent": "#8AB4F8",
    "black": "#000",
    "white": "#FFF",
    "green": "#6A994E",
    "blue": "#2191FB",
    "red": "#C33C54",
    "purple": "#AF47D2",
    "cyan": "#0E9594",
    "yellow": "#FFD60A",
}

layouts = [
    layout.Columns(
        border_focus=colors["accent"],
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=4,
        margin=4
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="monospace",
    fontsize=18,
    icon_size=24,
    padding=12,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=20,
                    highlight_method="block",
                    this_current_screen_border=colors["green"],
                    other_screen_border=colors["red"],
                    this_screen_border=colors["red"],
                    other_current_screen_border=colors["green"],
                    padding=4,
                ),
                widget.Prompt(
                    prompt="$ ",
                    font="monospace",
                    foreground=colors["green"],
                    cursor_color="#FFF",
                    background="#000",
                    padding=4,
                ),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                extra_widget.StatusNotifier(),
                # widget.Systray(),
                widget.Spacer(widget_defaults["padding"]),
                widget.TextBox(
                    text="",
                    mouse_callbacks={
                        "Button1": lambda : qtile.spawn(
                            os.path.expanduser("~/.config/qtile/scripts/wallpaper_cycle.sh --next")
                        ),
                        "Button3": lambda : qtile.spawn(
                            os.path.expanduser("~/.config/qtile/scripts/wallpaper_cycle.sh --prev")
                        ),
                        "Button2": lambda : qtile.spawn(
                            os.path.expanduser("~/.config/qtile/scripts/wallpaper_cycle.sh --rand")
                        ),
                    }
                ),
                widget.Net(
                    format="{down:>6.1f}{down_suffix:>2}  {up:>6.1f}{up_suffix:>2} ",
                ),
                extra_widget.WiFiIcon(
                    interface="wlp2s0",
                    padding_x=12,
                    padding_y=8,
                    wifi_arc=90,
                ),
                custom_widget.PulseVolume(
                    emoji=True,
                    emoji_list=["󰝟", "󰕿", "󰖀", "󰕾"],
                ),
                extra_widget.UPowerWidget(
                    battery_height=12,
                    battery_width=24,
                    margin=12,
                    percentage_low=0.3,
                    percentage_critical=0.2,
                ),
                widget.Clock(format="%a %d %b %H:%M"),
                widget.CurrentLayoutIcon(scale=0.8),
            ],
            32,
            # background=colors["bg"],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
floats_kept_above = True
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# Auto start applications
@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.Popen([script])

