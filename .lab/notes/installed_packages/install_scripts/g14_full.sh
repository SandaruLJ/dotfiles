#!/bin/bash

cat ../{common/{base,supplement}/{aur,official},g14_specific/{g14,official}}.txt | yay -S --needed - 
