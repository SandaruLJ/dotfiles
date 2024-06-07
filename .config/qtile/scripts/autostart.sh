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
