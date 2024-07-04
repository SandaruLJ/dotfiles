#!/bin/bash

wpaperctl next &

running_convertions=$(
    ps -ef | grep -iE 'magick.*/tmp/lockscreen.png' | grep -v 'grep' | tr -s ' ' | cut -d' ' -f2
)

if [ -n "$running_convertions" ]; then
    kill "$running_convertions"
fi

sleep 0.1
magick "$(wpaperctl get-wallpaper eDP-1)" -resize 1920x1080\> -blur 0x5 /tmp/lockscreen.png

