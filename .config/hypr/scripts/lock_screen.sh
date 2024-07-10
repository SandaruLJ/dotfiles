#!/bin/bash

hyprlock && killall swayidle &
swayidle -w timeout 30 'hyprctl dispatch dpms off'

