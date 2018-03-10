import nmap
import os
from socket import *
import checkopenports
from threading import Thread

nm=nmap.PortScanner()  #creates object

#scanning the subnet for connected IPs
data=nm.scan(hosts="172.16.163.*",arguments="-sP")

print("Number of connected IPs: {} ".format(data['nmap']['scanstats']['uphosts']))

#storing List of IPs
a=[ip for ip in data['scan']]

print("\n\tList of IPs Connected :")

print("------------------------------------------------------")

for i in a:
    
    print("\t{}IP connected: {}{}".format("|",i,"|"))

 print("-------------------------------------------------------")

#Scanning Ports
for i in a:
    
    print("Scanning {}".format(i))
    
    port=[80,21,29,8090,25,443,445,14147,3306]
    
    for j in port:
        #creating threads
        t=Thread(target=checkopenports.checkPort,args=(i,str(j)))
        
        t.start()
