#-*- coding: cp950 -*-
#-*- coding: utf-8 -*-

import sys
import binascii


try:
	md5file = open(sys.argv[1], "r").readlines()
except:
	print "[+] 使用方式   xxx.py    md5passfile"
	sys.exit(-1) 
	
for y in md5file:
	y=y[5:-1]
	y=binascii.b2a_hex(y.decode("base64"))
	print y
	
