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
        print(f"ERROR: Invalid IP format. Correct format: \n\n``` \n '0-255'.'0-255'.'0-255'.'0-255'/'1-32' \n                                     ```")
        return 2

    network = ipaddress.ip_network(INPUT, strict=False)

    for ip in network.hosts():
        print(ip)
        output = subprocess.run(['ping', f"{ip}", '-c', '1', '-W', '.05'])#, text=True capture_output=True ) ### Send to stdout & stderr
        
        ### Detect if network is UP or DOWN

function()

