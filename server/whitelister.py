#!/usr/bin/env python

import os

MAC_FILE_LOCATION = 'MACS.txt'
IP_FILE_LOCATION = 'IPS.txt' 


def reset():
	call('iptables --flush')
	call('iptables -I INPUT -p tcp --dport 1:10000 -j DROP')
	
        print('\n\nSetting up MACS.txt')
        whitelistMacs(getMacList())

        print('\n\nSetting up IPS.txt')
        whitelistips(getIpList())

def getMacList():
	macFile = open(MAC_FILE_LOCATION,'r')
	macFileRaw = macFile.read()
	macList = [x for x in macFileRaw.split('\n') if len(x) == 17]
        return macList

def getIpList():
	ipFile = open(IP_FILE_LOCATION,'r')
	ipFileRaw = ipFile.read()
	ipList = [x for x in ipFileRaw.split('\n') if '.' in x]
	return ipList

def whitelistMacs(macList):
	
	#JUST in case something happens
	if len(macList) <= 1: 
		return
	
	
	for mac in macList:
		call('iptables -I INPUT -p tcp --dport 1:10000 -m mac --mac-source ' + mac + ' -j ACCEPT')
	
	call('iptables -I INPUT -p tcp --dport 10000:60000 -j ACCEPT')

def whitelistips(iplist):
	print(iplist)
	if len(iplist) == 0:
		return
	for ip in iplist:
		call('iptables -I INPUT -p tcp --dport 1:10000 -s '+ip+' -j ACCEPT')	

def done():
	print 'Done'
def call(command):
	print('RUNNING: '+command)
	os.system(command)

