import socket

s = socket.socket()
Server = ''
Port = 8888
s.connect((Server,Port))
print (s.recv(1024))
s.close()
