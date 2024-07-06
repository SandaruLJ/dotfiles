#!/bin/bash

ac=$(udevadm info --path=/sys/class/power_supply/AC0 | grep POWER_SUPPLY_ONLINE | cut -d'=' -f 2)

if [ $ac -eq 0 ]; then
    systemctl suspend
fi

