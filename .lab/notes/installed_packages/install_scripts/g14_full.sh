#!/bin/bash

sudo multilibLine=$(grep -n "\[multilib\]" /etc/pacman.conf | cut -d":" -f1)
let "multilibIncludeLine = $multilibLine + 1"
sudo sed -i "${multilibLine}s|#||" /etc/pacman.conf
sudo sed -i "${multilibIncludeLine}s|#||" /etc/pacman.conf

cat ../{common/{base,supplement}/{aur,official},g14_specific/{g14,official}}.txt | yay -S --needed - 
