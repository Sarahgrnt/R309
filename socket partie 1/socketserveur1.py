import socket


server_socket = socket.socket()
server_socket.bind(("127.0.0.1", 10000))
print('serveur démaré')
server_socket.listen(1)
conn, address = server_socket.accept()
msg=""
test=""

while msg !="arret" and test!="arret":
    msg = conn.recv(1024).decode()
    print(msg)
    test= input("message:")
    conn.send(test.encode())



server_socket.close()
conn.close()



# conn.close() fermeture de la connexion client :bye (on recommence a partir du conn accept)
#server_socket.close() fermeture de la connexion serveur : arret