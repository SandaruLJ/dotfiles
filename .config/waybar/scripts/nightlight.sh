#!/bin/sh

FIFO='/tmp/waybar_nightlight'

main() {
    case $1 in
        'subscribe')
            subscribe
            ;;
        'toggle')
            toggle
            ;;
        *)
            echo 'Usage: <program> subscribe|toggle'
            ;;
    esac
}

subscribe() {
    # Create FIFO if it doesn't exist
    if [ ! -p $FIFO ]; then
        mkfifo $FIFO
    fi

    # Print initial gammastep state
    print_state

    # Tail the FIFO to listen to period changes
    tail -f $FIFO
}

toggle() {
    pkill gammastep || gammastep &
}

print_state() {
    if pidof gammastep > /dev/null; then
        state=$(gammastep -p 2>&1 | grep 'Notice: Period:' | cut -d ' ' -f 3 | tr A-Z a-z)
    else
        state='none'
    fi

    echo "{\"alt\": \"$state\", \"text\": \"$state\"}"
}

main "$@"

