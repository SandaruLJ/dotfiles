#!/bin/bash

cat ../g14_specific/{g14,official}.txt | sudo pacman -S --needed - 
