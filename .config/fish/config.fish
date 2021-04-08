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

starship init fish | source
