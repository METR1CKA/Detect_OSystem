#!/usr/bin/python3
# coding: utf-8

import sys, time, re, subprocess, socket

def slp():
    time.sleep(1)
    return

def checkTTL(ip):
    # Ping to get data
    proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip, ""], stdout=subprocess.PIPE, shell=True)
    # Get elements in string
    (out, err) = proc.communicate()
    # Split string to convert array
    out = out.split()
    # Decode element obtained
    out = out[12].decode('utf-8')
    # TTL
    ttl = re.findall(r"\d{1,3}", out)[0]
    # Return info
    return ttl

def osSystem(ttl):
    # Convert TTL to INT
    ttl = int(ttl)
    # Chech if ttl is Linux
    if ttl >= 0 and ttl <= 64:
        return "Linux"
    # Chech if ttl is Windows
    if ttl >= 65 and ttl <= 128:
        return "Windows"
    # Return not found system
    return "System not found"

def portsSystem(ip):
    # Get hostname by ip
    hostname = socket.gethostbyname(ip)
    # List for save ports
    ports = []
    # try/except to Exception
    try:
        # Check ports
        for port in range(1, 150):
            # Socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            # Save results
            results = s.connect_ex((hostname, port))
            # Save ports
            if results == 0:
                ports.append(port)
            # Close socket
            s.close()
            # Return ports
            return ports
    except Exception as error:
        # Return error
        return error

# Check if this is main
if __name__ == "__main__":
    # try/except to keyboard interrupt (CTRL + c)
    try:
        # Get ip
        ip = input("\n[+] Enter the ip address: ")
        # Check length
        if len(ip) == 0:
            print("\n[x] Error: No value entered for <ip>")
            sys.exit(1)
        # Get data
        ttl = checkTTL(ip)
        os = osSystem(ttl)
        ports = portsSystem(ip)
        # Print data
        print(
            f"""
            \n[*] ip: {ip}
            \n[*] ttl: {ttl}
            \n[*] os: {os}
            \n[*] open_ports: {ports}
            """
        )
        # Finish
        sys.exit(0)
    except KeyboardInterrupt:
        # Exception CTRL + c
        print("\n[!] Canceling process")
        slp()
        sys.exit(1)
