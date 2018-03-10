from socket import *
import optparse
import nmap
from threading import Thread,Semaphore
screenlock=Semaphore(value=1)

def checkPort(source,portlist):
	soc=gethostbyname(source)
	#print(soc)
	nm=nmap.PortScanner()
	nm.scan(soc,portlist)
	print(nm[soc].hostname())
	state=nm[soc]['tcp'][int(portlist)]['state']
	print("{} {} state: {}".format(soc,portlist,state))

'''if __name__=='__main__':
	
	port=[80,21,29,8090,25,443,445,14147,3306]
	for i in port:
		t=Thread(target=checkPort,args=("www.google.com",str(i)))
		t.start()
		
'''