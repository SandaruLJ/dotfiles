#!/bin/bash

LOCKSCR_PATH="/tmp/lockscreen.png"
LOCKSCR_GEN_DELAY=0.1

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

    if [[ -f $LOCKSCR_PATH ]]; then
        rm $LOCKSCR_PATH
    fi

    if [[ "$image_extension" != "PNG" ]]; then
        # Convert non-PNG files since hyprlock currently only supports PNGs
        kill_running_convertions
        magick "$current_wallpaper" -resize 1920x1080\> $LOCKSCR_PATH
    else
        # Otherwise, just link the file
        ln -s "$current_wallpaper" $LOCKSCR_PATH
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

kill_running_convertions() {
    pkill -f "magick.*$LOCKSCR_PATH"
}

main "$@"

