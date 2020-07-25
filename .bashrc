#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# Source aliases from .alias file
if [[ -s ".bash_aliases" ]]; then
    source .bash_aliases
fi

# Erase duplicates from history
HISTCONTROL=erasedups
