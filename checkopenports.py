from socket import *

import nmap

def checkPort(source,portlist):
	
	soc=gethostbyname(source)
	
	nm=nmap.PortScanner()
	
	#scanning for open ports
	nm.scan(soc,portlist)
	
	print(nm[soc].hostname())
	
	state=nm[soc]['tcp'][int(portlist)]['state']
	
	print("{} {} state: {}".format(soc,portlist,state))
