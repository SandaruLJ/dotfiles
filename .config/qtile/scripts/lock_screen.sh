#!/bin/bash

scrot /tmp/lockscreen.png
convert /tmp/lockscreen.png -blur 0x5 /tmp/lockscreen.png
i3lock -i /tmp/lockscreen.png
rm /tmp/lockscreen.png

