# Source aliases
if test -f .bash_aliases
    and test -r .bash_aliases
    source .bash_aliases
end

# Source temporary aliases
if test -f .bash_aliases_tmp
    and test -r .bash_aliases_tmp
    source .bash_aliases_tmp
end

# Enable Starship prompt if in GUI
if test $DISPLAY
    starship init fish | source
end

# Enable coloured output for man-pages
set -x LESS_TERMCAP_mb (printf '\033[01;31m')     # begin blink
set -x LESS_TERMCAP_md (printf '\033[01;36m')     # begin bold
set -x LESS_TERMCAP_me (printf '\033[0m')         # reset bold/blink
set -x LESS_TERMCAP_so (printf '\033[01;33m')     # begin reverse video
set -x LESS_TERMCAP_se (printf '\033[0m')         # reset reverse video
set -x LESS_TERMCAP_us (printf '\033[1;32m')      # begin underline
set -x LESS_TERMCAP_ue (printf '\033[0m')         # reset underline

