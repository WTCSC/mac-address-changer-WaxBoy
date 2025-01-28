import sys
import ipaddress
import os
import re
import subprocess


def function():
    #make sure input is used correctly
    if len(sys.argv) != 2:                                                        #takes just the filename not the whole path.    
        print(f"ERROR: Input should look as follows: \n\n    ``` \n        python3 {os.path.basename(__file__)} 'ip' \n                            ```")
        return 1
    INPUT = sys.argv[1]

    if not re.search(r"^(\d{1,3}[.]){3}\d{1,3}[/]\d{1,2}$", INPUT):
        print(f"ERROR: Invalid IP format. Correct format: \n\n``` \n '255'.'255'.'255'.'255'/'32' \n                                     ```")
        return 2

    network = ipaddress.ip_network(INPUT, strict=False)

    DOWN = 0
    UP = 0
    COUNT = 0

    for ip in network.hosts(): #only send 1 packet and only wait 10ms for a response   #captures output as byte string and turns it into text
        PING = subprocess.run(['ping', f'{ip}', '-c', '1', '-W', '.01'], text=True, capture_output=True) 
        output = PING.stdout
        if '0 received' not in PING.stdout:
            print(PING.stdout)
        else:
            print(ip)
        if PING.returncode == 0:
            UP += 1
        else:
            DOWN += 1
        
        
        COUNT += 1
    print(f"{UP} + {DOWN} = {COUNT}")
        ### Detect if network is UP or DOWN

function()

