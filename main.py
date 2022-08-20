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

    print('\n[+] ip: %s\n[+] ttl: %s\n[+] os: %s\n[+] open ports: %s' % (ip, ttl, os, ports))

except KeyboardInterrupt:

    print('\n[!] Canceling process')
    
    time.sleep(1)
    
    sys.exit(0)

