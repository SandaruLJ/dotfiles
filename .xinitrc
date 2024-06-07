#!/bin/bash

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

export GDK_BACKEND=x11
export WINIT_X11_SCALE_FACTOR=1

# set systemd user environment variables (environment.d)
while read -r var; do
    eval export $var
done < <(/usr/lib/systemd/user-environment-generators/30-systemd-environment-d-generator)

exec qtile start

