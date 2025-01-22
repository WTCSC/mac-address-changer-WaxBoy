#Take 2 inputs
INTERFACE=$1
NEWADDY=$2
if ip link show | grep -q  "$INTERFACE:"; then
    echo "Interface: $INTERFACE"
else
    echo "Error: Invalid Interface"
    exit 1
fi

#this function looks at the ips but only grabs the info from the specified interface, the info is then filtered to only grab mac addresses. Since there are going to be 2, head only takes the first one.
ADDY=$(ip link show $INTERFACE| grep -oE -m1 '([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}' | head -n 1)

echo "Initial Address: $ADDY"
echo "$ADDY" >> ./history.txt


#check if new address is in a valid format
if [[ "$NEWADDY" == "default" ]]; then

    if [[ -n $(ip link show $INTERFACE | grep -oE -m1 'permaddr ([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}' | awk '{print $2}') ]]; then
        NEWADDY=$(ip link show $INTERFACE | grep -oE -m1 'permaddr ([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}' | awk '{print $2}')
    else
        echo "Error: MAC address already factory default"
        exit 2
    fi

elif [[ ! "$NEWADDY" =~ ^([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}$ ]]; then
    echo "Error: '$NEWADDY' is not a valid address" >&2
    exit 3
fi
    
    sudo ip link set "$INTERFACE" address "$NEWADDY"
    echo "Success! New Address: $NEWADDY"
    exit 0

#create randomization for first 8-bit number or just use 02:
    #first number cannot be odd and first number cannot end in 0 or 8. (eg. 00, 08, F8, 20, 38, etc.)
#create randomization function for last 5 numbers
