#!/bin/bash

cat ../common/base/{aur,official}.txt | yay -S --needed - 
