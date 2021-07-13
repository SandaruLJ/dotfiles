#!/bin/bash

cat ../common/{base,supplement}/{aur,official}.txt | yay -S --needed - 
