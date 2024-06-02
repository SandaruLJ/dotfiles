#!/bin/bash

# workaround for filenames with spaces
IFS=$'\n'

current_wall=$(grep "/home" ~/.fehbg | cut -d " " -f 4- | cut -d "'" -f 2)
wall_dir=~/Pictures/SHARED/Wallpapers
walls=$(find $wall_dir -type f)

total_walls=0
for wall in $walls; do total_walls=$(($total_walls + 1)); done

wall_no=1
for wall in $walls; do
    if [[ $wall == $current_wall ]]; then
        current_wall_found=true
        break
    fi
    wall_no=$((wall_no + 1))
done

if [[ $1 == "--next" ]]; then
    if [[ $current_wall_found == true ]] && [[ $wall_no != $total_walls ]]; then
        feh --bg-fill "$(for wall in $walls; do echo $wall; done | sed -n $((wall_no + 1))p)"
    else
        feh --bg-fill "$(for wall in $walls; do echo $wall; done | head -n 1)"
    fi
elif [[ $1 == "--prev" ]]; then
    if [[ $current_wall_found == true ]] && [[ $wall_no != 1 ]]; then
        feh --bg-fill "$(for wall in $walls; do echo $wall; done | sed -n $((wall_no - 1))p)"
    else
        feh --bg-fill "$(for wall in $walls; do echo $wall; done | tail -n 1)"
    fi
elif [[ $1 == "--rand" ]]; then
    feh --bg-fill --randomize $wall_dir/*
else
    echo -e "No option specified.\n"\
            "\t--next\tchange to next wallpaper\n"\
            "\t--prev\tchange to previous wallpaper\n"\
            "\t--rand\tchange to a random wallpaper"
fi

