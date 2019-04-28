#!/usr/bin/python

from  socket import *

ports = range(1, 65536)
ip = raw_input("Insert IP Address:")
for i in ports:
	try:
		s = socket()
		s.connect((ip, i))
		s.send("\n\r")
		banner = s.recv(2048)
		s.close
		print "Port", i, "is open"
		print banner
	except:
		print i, "Close"


