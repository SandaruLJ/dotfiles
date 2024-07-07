#!/bin/sh

FIFO='/tmp/waybar_nightlight'

case $1 in
    'period-changed')
        echo "{\"alt\": \"$3\", \"text\": \"$3\"}" > $FIFO
esac

