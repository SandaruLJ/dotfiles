#!/usr/bin/env bash

event=$1
status=$2
ac_stat=$(acpi -a | cut -d" " -f3);
level=$(acpi -b | cut -d" " -f4 | sed 's/[^0-9]*//g');

case $event in
    "ac")
        case $status in
            "plugged"|"unplugged")
                battery-notify $status;
                ;;
        esac
        ;;

    "battery")
        case $status in
            "low")
                if [[ $ac_stat == "off-line" ]]; then
                    battery-notify $status $level;
                fi
                ;;

            "charged")
                if [[ $ac_stat == "on-line" ]]; then
                    battery-notify $status $level;
                fi
                ;;
        esac
        ;;
esac
