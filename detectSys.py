#!/usr/bin/python3
#coding: utf-8

import re, sys, subprocess
import socket

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

	def portsSys(self):
		hostname = socket.gethostbyname(self.ip)

		ports = []

		try:

			for port in range(1,150):

				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

				socket.setdefaulttimeout(1)

				results = s.connect_ex((hostname, port))

				if results == 0:

					ports.append(port)

				s.close()

			return ports

		except Exception as e:

			print('\n error {}'.format(e))

			sys.exit(0)
