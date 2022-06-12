### Overrides (incl. enabling coloured output)
alias ls='ls --color=auto --group-directories-first'
alias grep='grep --color=auto'
alias ip='ip --color=auto'
alias rm='trash'
alias cat='bat'

# Override 'bat' with 'batcat' on Debian-based systems
if test -f "/etc/debian_version"; then
    alias cat='batcat'
fi

### Helpful Queries
alias gpuinfo='lspci -k | grep -EA3 "VGA|3D|Display"'
alias myip='curl icanhazip.com'

## Memory Management
alias memmon='watch -n 1 free -h'
alias swapflush='sudo swapoff -av && sudo swapon -av'
alias pagecacheflush='echo 1 | sudo tee /proc/sys/vm/drop_caches >/dev/null; echo "Page cache dropped"'

## Config Shortcuts
alias bash-config='vim ~/.bashrc'
alias fish-config='vim ~/.config/fish/config.fish'
alias refind-config='sudo vim /boot/efi/EFI/refind/manual.conf'
#alias zsh-config='vim ~/.zshrc'

## VM Management
# Arch Linux
alias archlinux-start='virsh start archlinux && virt-viewer -af archlinux'
alias archlinux-shutdown='virsh shutdown archlinux'
alias archlinux-save='virsh save archlinux /var/tmp/kvm-saves/archlinux'
alias archlinux-restore='virsh restore /var/tmp/kvm-saves/archlinux && virt-viewer -af archlinux'
# Windows
alias windows-start='virsh start win10 && virt-viewer -af win10'
alias windows-shutdown='virsh shutdown win10'
alias windows-save='virsh save win10 /var/tmp/kvm-saves/win10'
alias windows-restore='virsh restore /var/tmp/kvm-saves/win10 && virt-viewer -af win10'

## Other
alias dotfiles='git --git-dir=$HOME/.lab/git/dotfiles --work-tree=$HOME'
#alias primerun='__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia '

