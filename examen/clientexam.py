import socket
import threading
PORT=10058
msg=""
data = ""
msgcl=""
msgserv = ""



def connected(self):
    client_socket = socket.socket()
    print("En attente de connexion")
    client_socket.connect((self.__hostname, self.__port))
    print("Connexion établie")

def reception(client_socket):
    msgserv = ""
    while msgserv != "bye" and msgserv != "arret":
        msgserv = client_socket.recv(1024).decode()
        print(msgserv)


if __name__ =="__main__":


    client_socket = socket.socket()
    client_socket.connect(("127.0.0.1", 10058))
    print ("connecté au serveur")

    t = threading.Thread(target= reception,args=[client_socket])
    t.start()

    while msgcl !="bye":
        msgcl = str(input("message:"))
        envoie = client_socket.send(msgcl.encode())

    t.join()

    client_socket.close()