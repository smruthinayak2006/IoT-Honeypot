import socket

client = socket.socket()

client.connect(("localhost",2323))

data = client.recv(1024)

print(data.decode())

client.close()