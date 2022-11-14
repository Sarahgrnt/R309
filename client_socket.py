import socket


client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 10000))
print ("connecté au serveur")
client_socket.send(input().encode())
data = client_socket.recv(1024).decode()
if data == "stop":
    client_socket.close()
else:
    client_socket.send(input().encode())
print(data)
client_socket.close()