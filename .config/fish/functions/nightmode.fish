function nightmode --description "Toggle nightmode: 'on' | 'off'"
    set invalid_options "Please provide options 'on' or 'off'"
    if count $argv > /dev/null
        if [ $argv[1] = "on" ]
            set bold_is_bright true
            set bat_theme "OneHalfDark"
        else if [ $argv[1] = "off" ]
            set bold_is_bright false
            set bat_theme "OneHalfLight"
        else
            echo $invalid_options
            return 1
        end
    else
        echo "Please provide options 'on' or 'off'"
        return 1
    end

    # Set Gnome Terminal settings
    gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:b1dcc9dd-5262-4d8d-a863-c897e6d979b9/ bold-is-bright $bold_is_bright

    # Set bat theme settings
    sed -i "s/\(--theme *= *\).*/\1\"$bat_theme\"/" ~/.config/bat/config
end
