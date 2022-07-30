#!/usr/bin/python3
#coding: utf-8

import re, sys, subprocess

class detectSystem:

	def __init__(self, ip):
		self.ip = ip

	def checkTTL(self):
		proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % self.ip, ""], stdout = subprocess.PIPE, shell = True)

		(out, err) = proc.communicate()

		out = out.split()

		out = out[12].decode('utf-8')

		ttl = re.findall(r"\d{1,3}", out)[0]

		return ttl

	def osSystem(self, ttl):

		ttl = int(ttl)

		os = ''

		if ttl >= 0 and ttl <= 64:
			os = 'Linux'
		elif ttl >= 65 and ttl <= 128:
			os = 'Windows'
		else:
			os = 'System not found'

		return os
