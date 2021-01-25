# Source aliases
if test -f .alias
    and test -r .alias
    source .alias
end

starship init fish | source
