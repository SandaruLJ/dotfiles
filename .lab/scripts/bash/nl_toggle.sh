#!/usr/bin/env bash

export DISPLAY=":0";
export XAUTHORITY="/home/sandarulj/.Xauthority";
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus";

nl_gsetting='org.gnome.settings-daemon.plugins.color night-light-enabled'
nl_on='dunstify "Night Light On" "Night Light has been turned on" -i night-light -h int:transient:1 -A "turnOff, Turn Off Night Light" -b -p';
nl_off='dunstify "Night Light Off" "Night Light has been turned off" -i night-light -A "turnOn, Turn On Night Light" -b -p';
id_file='/tmp/nl_toggle.tmp';


turnOn() {
    gsettings set $nl_gsetting true;    

    if [[ ! -s $id_file ]]; then
        eval "$nl_on > $id_file";
    else
        notif_id=$(sed -n 1p $id_file);
        eval "$nl_on -r $notif_id > $id_file";
    fi

    action=$(sed -n 2p $id_file);

    case $action in
        "turnOff")
            turnOff;
            ;;
    esac

    rm $id_file;
}


turnOff() {
    gsettings set $nl_gsetting false;
    
    if [[ ! -s $id_file ]]; then
        eval "$nl_off > $id_file";
    else
        notif_id=$(sed -n 1p $id_file);
        eval "$nl_off -r $notif_id > $id_file";
    fi

    action=$(sed -n 2p $id_file);
    
    case $action in
        "turnOn")
            turnOn;
            ;;
    esac

    rm $id_file;
}


if $(gsettings get $nl_gsetting); then
    turnOff;
else
    turnOn;
fi

