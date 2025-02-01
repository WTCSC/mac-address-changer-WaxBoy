import sys
import subprocess
import re
import random

def macchanger():
    #Define the eternal trash can
    TRASH = subprocess.DEVNULL

    #Grab INTERFACE and output from `ip link show $INTERFACE`
    INTERFACE = sys.argv[1]
    iplinkshow = subprocess.run(['ip', 'link', 'show', f'{INTERFACE}'], capture_output=True, text=True).stdout
    
    ##ERROR 2: Invalid Interface
    if f' {INTERFACE}: <' not in iplinkshow:
        print("ERROR: Invalid Interface")
        return 2
    ####print(iplinkshow)
    
    #Find MAC address in iplinkshow
    match = re.search(r'([0-9a-f]{2}:){5}[0-9a-f]{2}', iplinkshow)
    
    ##ERROR 3: No MAC address found
    if not match:
        print("ERROR: No MAC address found")
        return 3    
    
    #get Output from match object
    MAC = match.group()
    ####print(MAC)

    #grab INPUT from cmd line
    INPUT = sys.argv[2]
    ####print(INPUT)

    #check if INPUT is valid MAC address
    if not re.search(r'[0-9a-f][02468ACE](:[0-9a-f]{2}){5}', INPUT):
        
        ##ERROR 4: Bad format
        if INPUT != 'default':
            if INPUT == 'random':
                f"{random.getrandbits(4):x}{['0','2','4','6','8','a','c','e'][random.getrandbits(3)]}:{random.getrandbits(8):02x}:{random.getrandbits(8):02x}:{random.getrandbits(8):02x}:{random.getrandbits(8):02x}:{random.getrandbits(8):02x}"
            else:
                print("ERROR: Invalid MAC Address Format")
                return 4
        
        #get Default MAC address
        INPUT = (subprocess.run(['ethtool', '-P', f'{INTERFACE}'], capture_output=True, text=True).stdout[19:-1])
        
        ##ERROR 5: Address at factory default already
        if INPUT == MAC:
            print(f"ERROR: MAC Address Already Defaulted")
            return 5
            
    #print pre-process details
    print(f"Interface:  {INTERFACE}\n\nInitial MAC address:  {MAC}\n")
    
    #set MAC address
    swap = subprocess.run(['sudo', 'ip', 'link', 'set', f'{INTERFACE}', 'address', f'{INPUT}'], stderr=TRASH, stdout=TRASH)

    ##If it fails give ERROR 6: Misc subprocess error
    if swap.returncode > 0:
        print("Subprocess ERROR: Interface unavailable || MAC address invalid")
        return 6
    
    #User Feedback
    print(f"Updated Address:  {INPUT}") 

#call function
macchanger()
