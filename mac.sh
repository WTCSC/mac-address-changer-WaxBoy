#Take 2 inputs
INTERFACE=$1
NEWADDY=$2

#if no such INTERFACE is detected by the device throw error
if ip link show | grep -q  "$INTERFACE:"; then
    echo "Interface: $INTERFACE" 
else
    echo "Error: Invalid Interface"
    exit 1
fi

#this function looks at the addresses but only grabs the info from the specified interface. 
#the info is then filtered to only grab mac addresses. Since there will be atleast 2, head only takes the first one.
ADDY=$(ip link show $INTERFACE| grep -oE -m1 '([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}' | head -n 1)


#if default, check that address is not already set to its default
if [[ "$NEWADDY" == "default" ]]; then
    if [[ -n $(ip link show $INTERFACE | grep -oE -m1 'permaddr ([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}' | awk '{print $2}') ]]; then
        NEWADDY=$(ip link show $INTERFACE | grep -oE -m1 'permaddr ([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}' | awk '{print $2}')
    else
        echo "Error: MAC address already factory default"
        exit 2
    fi

    #if random, create a random address and set a variable which will prompt user confirmation before randomly setting the address
elif [[ "$NEWADDY" == "random" ]]; then
    NEWADDY=$(printf "02:%02x:%02x:%02x:%02x:%02x" $((RANDOM % 256)) $((RANDOM % 256)) $((RANDOM % 256)) $((RANDOM % 256)) $((RANDOM % 256)))
    CONFIRM=lol

    #if trying to put in an address, it must in proper xx:xx:xx:xx:xx:xx format
elif [[ ! "$NEWADDY" =~ ^([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}$ ]]; then
    echo "Error: '$NEWADDY' is not a valid address" >&2
    exit 3
fi

#System feedback
echo "Initial Address: $ADDY"

if [[ -n $CONFIRM ]]; then
    read -p "Are you sure you want to change your MAC address to $NEWADDY? (Type Y or YES to confirm): " CONFIRM2
    if [[ ! ( ${CONFIRM2,,} == "yes" || ${CONFIRM2,,} == "y" ) ]]; then
        echo "Confirmation Failed"
        exit 4
    fi
fi



#if everything so far has gone right, the function will not have exited and the MAC switch can be made.

#if the MAC address has not been recorded, place it in history.
if [[ -z $(grep "$INTERFACE | $ADDY" ./history.txt) ]]; then
    echo "$INTERFACE | $ADDY" >> ./history.txt
fi

#Congrats! You have a new MAC address
sudo ip link set "$INTERFACE" address "$NEWADDY"
echo "Success! New Address: $NEWADDY"


#create randomization for first 8-bit number or just use 02:

#create randomization function for last 5 numbers
