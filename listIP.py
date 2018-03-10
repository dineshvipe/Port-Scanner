import nmap
import os
from socket import *
import checkopenports
from threading import Thread

nm=nmap.PortScanner()
data=nm.scan(hosts="172.16.163.*",arguments="-sP")
print("Number of connected IPs: {} ".format(data['nmap']['scanstats']['uphosts']))
#print(data['scan'])
a=[ip for ip in data['scan']]
#print(a)
print("\n\tList of IPs Connected :")
print("------------------------------------------------------")
for i in a:
    print("\t{}IP connected: {}{}".format("|",i,"|"))
print("-------------------------------------------------------")
for i in a:
    #print("\tIP: {}".format(i))
    print("Scanning {}".format(i))
    port=[80,21,29,8090,25,443,445,14147,3306]
    for j in port:
        t=Thread(target=checkopenports.checkPort,args=(i,str(j)))
        t.start()