### Default
alias ls='ls --color=auto --group-directories-first'
alias vi='vim'


### Custom
alias gpuinfo='lspci -k | grep -EA1 "VGA|3D|Display"'
alias refind-config='sudo vim /efi/EFI/refind/refind.conf'
alias grep='grep --color=auto'
alias untar='tar xvf'

## Memory Management
alias memmon='watch -n 1 free -h'
alias swapflush='sudo swapoff -av && sudo swapon -av'
alias pagecacheflush='echo 1 | sudo tee /proc/sys/vm/drop_caches >/dev/null; echo "Page cache dropped"'

## Shell Config Shortcuts
alias bash-config='vim ~/.bashrc'
alias fish-config='vim ~/.config/fish/config.fish'
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
alias myip='curl icanhazip.com'
#alias primerun='__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia '

# Load machine specific aliases
if [[ -s ".bash_aliases_tmp" ]]; then
    source .bash_aliases_tmp
fi

