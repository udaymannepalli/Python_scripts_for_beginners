import socket

c = socket.socket()
c.connect(('localhost', 4444))
name = input('enter your name: ')
c.send(bytes(name, 'utf-8'))
print(c.recv(1024).decode())