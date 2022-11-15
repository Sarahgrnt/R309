import socket

client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 10000))
print ("connecté au serveur")
msg=""
while msg !="bye":
    msg = str(input("message:"))
    envoie = client_socket.send(msg.encode())
    data = client_socket.recv(1024).decode()
    print(data)

client_socket.close()