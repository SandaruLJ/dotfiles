#!/usr/bin/env bash

export DISPLAY=":0";
export XAUTHORITY="/home/sandarulj/.Xauthority";
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus";

status=${1,,};  # Converting $1 argument to lowercase
level=$2;
id_file="/tmp/battery_notify.tmp";
notif='dunstify -u critical -b -p > $id_file "Battery ${status^}" "$msg"';
notif_icon='-i battery-level-$(let num="($level+5)/10*10"; echo $num)';


if [[ ! -z $level && ($level -ge 0 && $level -le 100) ]]
then
    case $status in
        "low")
            msg="Level: $level% | Plug in to the AC"

            if [[ -s "$id_file" ]]; then
                eval "$notif $notif_icon -r $(cat $id_file)";
            else
                eval "$notif $notif_icon";
            fi
            ;;

        "charged")
            msg="Level: $level% | Unplug from the AC";

            if [[ $level -ge 95 ]]; then
                charge_stat="charged";
            else
                charge_stat="charging";
            fi

            if [[ -s "$id_file" ]]; then
                eval "$notif $notif_icon-$charge_stat -r $(cat $id_file)";
            else
                eval "$notif $notif_icon-$charge_stat";
            fi
            ;;
    esac

    if [[ -s "$id_file" ]]; then
        rm $id_file;
    fi

else
    case $status in
        "plugged"|"unplugged")
            if [[ -s "$id_file" ]]; then
                dunstify -C $(cat $id_file);
            fi
            ;;
    esac
fi
