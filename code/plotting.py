import socket, sys, os, smbus , math, random
from time import sleep

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print "create socket successful"
host = 'localhost'
port = 2220
s.bind((host, port))
s.listen(15)

print "socket binded to %s" %(port)

while True:
    c, addr = s.accept()
    print ('got connection from', addr)

    for x in range(0, 1000):
        c.send("x"+random.randrange(0, 300))
        c.close()
        
