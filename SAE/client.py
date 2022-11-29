import socket
PORT=10001
msg=""
data = ""

if __name__ =="__main__":


        while True:
            client_socket = socket.socket()
            client_socket.connect(("127.0.0.1", PORT))
            print ("connecté au serveur")

            while msg !="disconnect" and data != "disconnect" and msg !="kill" and data != "kill"and msg !="reset" and data != "reset":
                msg = str(input("message:"))
                envoie = client_socket.send(msg.encode())
                data = client_socket.recv(1024).decode()
                print(data)

            client_socket.close()
