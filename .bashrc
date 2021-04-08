#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# Source aliases from .bash_aliases file
if [[ -s ".bash_aliases" ]]; then
    source .bash_aliases
fi

# Source temporary aliases from .bash_aliases_tmp file
if [[ -s ".bash_aliases_tmp" ]]; then
    source .bash_aliases_tmp
fi

# Erase duplicates from history
HISTCONTROL=erasedups
