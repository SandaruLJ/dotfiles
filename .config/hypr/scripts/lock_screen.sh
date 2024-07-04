#!/bin/bash

hyprlock && killall swayidle &
swayidle -w timeout 10 'hyprctl dispatch dpms off'

