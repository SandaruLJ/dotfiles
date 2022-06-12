#!/usr/bin/env bash

iso="$1"

if [[ ! "$iso" ]]; then
    echo "Please specify an ISO file"
    exit 1
fi

qemu-system-x86_64 -name guest="$(basename "$iso")" \
      -machine pc-q35-6.2,vmport=off \
      -accel kvm \
      -cpu host \
      -m 2G \
      -smp 2,sockets=2,cores=1,threads=1 \
      -device virtio-vga-gl,xres=1920,yres=1080 \
      -device AC97 \
      -display sdl,gl=on,window-close=on \
      -boot d \
      -cdrom "$iso" \
      -net user -nic user,model=virtio-net-pci \
      -device virtio-keyboard-pci \
      -device virtio-tablet-pci


