#!/bin/bash

LOCKSCR_PATH="/tmp/lockscreen.png"
LOCKSCR_GEN_DELAY=0.5

main() {
    if [[ $1 == "init" ]]; then
        init_wallpaper
    elif [[ $1 == "next" ]]; then
        next_wallpaper
    else
        echo "Usage: <program> init|next"
    fi
}

init_wallpaper() {
    pidof wpaperd || wpaperd -d
    generate_lockscreen
}

next_wallpaper() {
    wpaperctl next &
    generate_lockscreen
}

generate_lockscreen() {
    current_wallpaper=$(get_current_wallpaper)
    image_extension=$(get_image_extension "$current_wallpaper")

    kill_running_tasks

    if [[ "$image_extension" != "PNG" ]]; then
        # Convert non-PNG files since hyprlock currently only supports PNGs
        magick "$current_wallpaper" -resize 1920x1080\> $LOCKSCR_PATH
    else
        # Otherwise, just copy the file
        cp "$current_wallpaper" $LOCKSCR_PATH
    fi
}

get_current_wallpaper() {
    screen_name=$(hyprctl monitors | head -n 1 | cut -d ' ' -f 2)

    while [ -z "$current_wallpaper" ]; do
        sleep $LOCKSCR_GEN_DELAY
        current_wallpaper=$(wpaperctl get-wallpaper $screen_name)
    done

    echo "$current_wallpaper"
}

get_image_extension() {
    file "$1" | cut -d ':' -f 2 | cut -d ' ' -f 2
}

kill_running_tasks() {
    pkill -f "(magick|cp).*$LOCKSCR_PATH"
}

main "$@"

