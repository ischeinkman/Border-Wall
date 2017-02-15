# Border-Wall
Secure your borders from hostile foreign entities.

#Preamble
Our servers are the best servers. Aren't they the best servers folks? But some people want to destroy our very file systems. 
They connect to the server, and no one knows anything about them. They're destroying our hard-earned bash jobs! We have to
keep them out, folks. We have to build a wall on our border.

#About
Border-Wall uses iptables to protect your server from bad actors on LAN. Without the password, key, and a valid user name,
your server becomes invisible. The server does not even respond to pings behind the wall. Only after authenticating with AES
can the client seamlessly access all services.

#Installation
Border-Wall requires python-crypto for AES encryption. Border-Wall's server software also requires IPTables for port blocking.

After all prerequisites are installed, clone the repository on both the client and server with:
```
git clone https://github.com/ischeinkman/Border-Wall.git
```

#Configuration
After installing, the wall needs to be configured. An example CONFIG.txt is provided in the repository and may be modified
as necessary. 

| Key | Description | Example |
|-----|-------------|---------|
|ip   | IP client will connect to. Does nothing for server. | 127.0.0.1 |
|port | Port to run server on. Must be greater than 10000.| 44444 |
|password | The password to use. | testpass |
|key | The key that will be provided to AES. | testkey |
|validusers| A comma separated list of valid user strings. | u1, u2, u3 |
|defaultuser | The default user string the client will connect with. Useless on server. | u1 |

#Running
On the server, the application may be run with 
```
python whitelistserver.py
```
The server requires root access to set up the firewall.

To connect to a server from a client, make sure you have a matching CONFIG.txt and run
```
python connectserver.py
```
