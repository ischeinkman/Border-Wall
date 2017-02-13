import socket
import os
import sys
import subprocess
from Crypto import Random
from Crypto.Cipher import AES

import whitelister

password = ''
key = b''

def decrypt(msg):
	salt = Random.new().read(16)
	cipher = AES.new(key, AES.MODE_CFB, salt)
	dehexed = msg.decode('hex')
	decrypted = cipher.decrypt(dehexed)
	return decrypted[16:]

def getIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def runserver(port):
    
    print('Creating socket')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = getIp()
    print('Binding to '+ip+':'+str(port))
    server_address = (ip, port)
    sock.bind(server_address)

    print('Listening')
    sock.listen(1)
    
    ipsToUsers = {}
        
    while True:
        conn, addr = sock.accept()
        try:
            msg = conn.recv(1024)
        except:
            continue
	conn.close()
	dmsg = decrypt(msg)
	print('MSG: '+dmsg)
	arglist = [x for x in dmsg.split(';') if x!='']
	if arglist[1] != password:
		print('WRONG PASS')
	else:
		srcip = addr[0]
                if len(arglist) >= 3:
			srcip = arglist[2]
                userid = arglist[0]
		ipsToUsers[userid] = srcip
		print(str(ipsToUsers))
		whitelister.reset()
		whitelister.whitelistips(ipsToUsers.values())	
		whitelister.done()
	
if __name__ == '__main__':
    whitelister.reset()
    whitelister.done()

    if len(sys.argv) > 2:
        sys.exit(0)
    if len(sys.argv) == 2:
        runserver(int(sys.argv[1]))
    else:
        runserver(44445)		
