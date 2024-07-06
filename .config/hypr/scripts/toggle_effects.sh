#!/bin/bash

disable_effects() {
    hyprctl --batch " \
        keyword animations:enabled 0; \
        keyword decoration:drop_shadow 0; \
        keyword decoration:blur:enabled 0; \
        keyword misc:vfr 1"

    notify-send -eu low "Effects Off" "Disabling animations and other fancy effects"
}

restore_effects() {
    hyprctl reload
    notify-send -eu low "Effects On" "Restoring configured effects"
}

if [[ $1 == "off" ]]; then
    disable_effects
elif [[ $1 == "on" ]]; then
    restore_effects
else
    # Check if animations are enabled
    FANCY_EFFECTS=$(hyprctl getoption animations:enabled | awk 'NR==1{print $2}')

    if [ "$FANCY_EFFECTS" = 1 ]; then
        # Disable effects
        disable_effects
        exit
    fi

    # Reload with default configs
    restore_effects
fi

