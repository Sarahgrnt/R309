import socket
msg=""
test=""
if __name__ =="__main__":
    server_socket = socket.socket()
    server_socket.bind(("127.0.0.1", 10005))
    print('serveur démaré')
    server_socket.listen(1)


    while msg !="arret" and test!="arret":
        conn, address = server_socket.accept()
        msg = ""
        test = ""
        while msg !="bye" and test!="bye" and msg !="arret" and test!="arret":
            msg = conn.recv(1024).decode()
            print(msg)
            if msg =="bye":
                conn.send("bye".encode())
            else:
                test= input("message:")
                conn.send(test.encode())
        conn.close()


    server_socket.close()




# conn.close() fermeture de la connexion client :bye (on recommence a partir du conn accept)
#server_socket.close() fermeture de la connexion serveur : arret