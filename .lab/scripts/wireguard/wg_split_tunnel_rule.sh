#!/bin/bash
# Required for split-tunneling the public IP of WireGuard server
# Workaround for NetworkManager not supporting PostUp, PreDown etc.
# Place this script under /etc/NetworkManager/dispatcher.d/ with executable
# permissions, then enable and start NetworkManager-dispatcher.service

INTERFACE=wg@jupiter
FWMARK=0xca6c
TABLE=51820

if [ "$1" = "$INTERFACE" ]; then
    if [ "$2" = "up" ]; then
        ip rule add not fwmark $FWMARK table $TABLE
    elif [ "$2" = "down" ]; then
        ip rule del not fwmark $FWMARK table $TABLE
    fi
fi

