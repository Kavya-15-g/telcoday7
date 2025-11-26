import subprocess
import os
ip_list = [
    "192.168.1.1",
    "8.8.8.8",
    "10.0.0.1",
    "192.168.56.1"
]
for ip in ip_list:
    print(f"Checking {ip} ...")
    
    # For Windows use: ping -n 1
    command = ["ping", "-n", "1", ip]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print(f"IP address {ip} is reachable.\n")
    else:
        print(f"IP address {ip} is unreachable.\n")