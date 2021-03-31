#!/usr/bin/python
 
from scapy.all import *
import sys

conf.verb=0

if (sys.argv[1]):
	print(".:              Ping Scann3r | Unc0dl3              :.")
	print(".: An ping scanner tool coded with python and scapy :.")
	print(".: Usage mode: pingscanner.py 000.000.000           :.")
	print(".: Example: sudo python3 pingscanner.py 192.168.15  :.")
else:
	for sufix in range(1, 255):
		ipRange  = "%s.%d" %(sys.argv[1], sufix)
		ip = IP(dst=ipRange)
		package = ip/ICMP()

		responses, noresponse = sr(package, timeout=1)

		for response in responses:
			print("[+] Host descoberto em %s" %response[1][IP].src)

