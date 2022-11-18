import threading
import socket
msgcl=""
msgserv = ""


def reception(server_socket):
    msgcl = ""
    while msgcl != "bye" and msgcl != "arret":
        msgcl = server_socket.recv(1024).decode()
        print(msgcl)


if __name__ =="__main__":
    server_socket = socket.socket()
    server_socket.bind(("127.0.0.1", 10000))
    print('serveur démaré')
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print('connexion client')




    t = threading.Thread(target=reception, args=[conn])
    t.start()

    while msgserv != "bye":
        msgserv = str(input("message:"))
        envoie = conn.send(msgserv.encode())

    t.join()

    server_socket.close()