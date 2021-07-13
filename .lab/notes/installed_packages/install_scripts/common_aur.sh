#!/bin/bash

cat ../common/{base,supplement}/aur.txt | yay -S --needed -
