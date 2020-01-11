import socket

s=socket.socket()
Server = 'localhost'
Port = 80
s.ind((Server,Port))
s.listen(5)

while True:
	c,adress = s.accept()
	print ("WE GOT CONNECTION FROM", address)
	c.send("You are Connected\n")
	c.close()