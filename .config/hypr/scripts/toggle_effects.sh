#!/bin/bash

# Check if animations are enabled
FANCY_EFFECTS=$(hyprctl getoption animations:enabled | awk 'NR==1{print $2}')

if [ "$FANCY_EFFECTS" = 1 ]; then
    # Disable effects
    hyprctl --batch " \
        keyword animations:enabled 0; \
        keyword decoration:drop_shadow 0; \
        keyword decoration:blur:enabled 0; \
        keyword misc:vfr 1"

    notify-send -u low "Effects Off" "Disabling animations and other fancy effects"

    exit
fi

# Reload with default configs
hyprctl reload

notify-send -u low "Effects On" "Restoring configured effects"

