#!/bin/bash

# wallpaper
if [[ -s "$HOME/.fehbg" ]]; then
    eval "$HOME/.fehbg" 
else
    feh --bg-fill --randomize ~/Pictures/SHARED/Wallpapers/* &
fi

# blue light filter
redshift &

# compositor
picom -b

# keyring
if (! pidof gnome-keyring-daemon); then
    dbus-update-activation-environment --all
    gnome-keyring-daemon --start
fi

# notification daemon
dunst &

# disk manager
udiskie &

