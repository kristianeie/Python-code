#!/usr/bin/python

import socket

target_host = "0.0.0.0"
target_port = 9999

# create a socket object with AF_INET and SOCK_STREAM. 
# AF_INET means the socket is going to use a standard IPv4 address. 
# SOCK_STREAM means it will be a TCP client 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client to server

client.connect((target_host, target_port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data

response = client.recv(4096)

print response
