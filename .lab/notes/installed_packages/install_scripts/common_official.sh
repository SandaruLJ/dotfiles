#!/bin/bash

cat ../common/{base,supplement}/official.txt | sudo pacman -S --needed -
