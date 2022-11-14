import socket


server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 10000))
print('serveur démaré')
server_socket.listen(1)
conn, address = server_socket.accept()
msg=""
while msg !="bye":
    msg = conn.recv(1024).decode()
    print(msg)
    test= input("message:")
    conn.send(test.encode())

conn.close()