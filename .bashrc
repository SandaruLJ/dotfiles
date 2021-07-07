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

# Enable coloured output for man-pages
export LESS_TERMCAP_mb=$'\E[1;31m'     # begin blink
export LESS_TERMCAP_md=$'\E[1;36m'     # begin bold
export LESS_TERMCAP_me=$'\E[0m'        # reset bold/blink
export LESS_TERMCAP_so=$'\E[01;33m'    # begin reverse video
export LESS_TERMCAP_se=$'\E[0m'        # reset reverse video
export LESS_TERMCAP_us=$'\E[1;32m'     # begin underline
export LESS_TERMCAP_ue=$'\E[0m'        # reset underline

