#!/bin/bash

cat ../common/supplement/{aur,official}.txt | yay -S --needed - 
