#!/bin/sh

FIFO='/tmp/waybar_nightlight'

case $1 in
    'period-changed')
        if [ ! -p $FIFO ]; then
            mkfifo $FIFO
        fi

        echo "{\"alt\": \"$3\", \"text\": \"$3\"}" >> $FIFO
esac

