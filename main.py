#!/usr/bin/python3
#coding: utf-8

from app.detectSys import detectSystem

import sys, time

try:

    ip = input('\n[+] Enter the ip address: ')

    obj = detectSystem(ip)

    ttl = obj.checkTTL()

    os = obj.osSystem(ttl)

    ports = obj.portsSys()

    print(
        f'''
        \n[+] ip: {ip}
        \n[+] ttl: {ttl}
        \n[+] os: {os}
        \n[+] open ports: {ports}
        '''
    )

except KeyboardInterrupt:

    print('\n[!] Canceling process')
    
    time.sleep(1)
    
    sys.exit(0)

