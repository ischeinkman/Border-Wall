#!/usr/bin/python

import socket
import sys

from Crypto.Cipher import AES
from Crypto import Random

password = ""
defaultid = ""
key = b''

ip = ''
port = -1

def createMsg(user, ip = None):
    
    if user == None:
        user = defaultid

    ipstring = ''
    if ip != None:
        ipstring = ';'+ip

    salt = Random.new().read(16)
    cipher = AES.new(key, AES.MODE_CFB, salt)
    encodedmsg = (salt + cipher.encrypt(user+';'+password+ipstring)).encode('hex')
    
    return encodedmsg

def authenticate(ip, port, user, srcip = None):
    print('Creating socket...')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting...')
    sock.connect((ip, port))
    print('Sending...')
    sock.send(createMsg(user, srcip))
    print('Sent.')
    sock.close()

def main():
    
    try:
        srcindex = sys.argv.index('-s')
        srcip = sys.argv[srcindex+1]
    except ValueError:
        srcip = ''

    try:
        userindex = sys.argv.index('-u')
        userid = sys.argv[userindex+1]
    except ValueError:
        userid = defaultid
    
    authenticate(ip, int(port), userid, srcip)

        

if __name__ == '__main__':
    main()
