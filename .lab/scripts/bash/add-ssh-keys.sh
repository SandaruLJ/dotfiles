#!/bin/bash

for key_file in $(find $HOME/.ssh -perm 600); do
   if [[ $key_file != *known_hosts* ]]; then 
       ssh-add -q $key_file
   fi
done
