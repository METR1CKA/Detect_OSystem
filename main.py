#!/usr/bin/python3
#coding: utf-8

import sys
from detectSys import detectSystem

if len(sys.argv) != 2:
    print('\n[!] uso: python3 ' + sys.argv[0] + ' <direccion ip>\n')
else:
    ip = sys.argv[1]

    obj = detectSystem(ip)

    ttl = obj.checkTTL()

    os = obj.osSystem(ttl)

    print('\n[*] ip: %s\n[*] ttl: %s\n[*] os: %s' % (ip, ttl, os))