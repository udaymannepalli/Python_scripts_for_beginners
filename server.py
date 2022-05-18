import socket

s = socket.socket()
print("Socket created")
s.bind(("localhost",4444))
s.listen(3)
print("waiting for connections")
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with ", addr, name)
    c.send(bytes("welcome to the chat room", 'utf-8'))
    c.close()