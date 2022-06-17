import socket

sock = socket.socket()
sock.connect(("localhost", 8989))
sock.send(b"hi")

data = sock.recv(1024)
sock.close()

print(data)
