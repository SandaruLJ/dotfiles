#!/bin/bash

# Set wallpaper
if [[ -s "$HOME/.fehbg" ]]; then
    eval "$HOME/.fehbg" 
else
    feh --bg-fill --randomize ~/Pictures/SHARED/Wallpapers/* &
fi

redshift &
picom -b

