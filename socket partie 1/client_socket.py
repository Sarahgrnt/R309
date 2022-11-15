import socket
msg=""
data = ""

if __name__ =="__main__":
    client_socket = socket.socket()
    client_socket.connect(("127.0.0.1", 10000))
    print ("connecté au serveur")

    while msg !="bye" and data != "bye" and msg !="arret" and data != "arret":
        msg = str(input("message:"))
        envoie = client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()
        print(data)

    client_socket.close()