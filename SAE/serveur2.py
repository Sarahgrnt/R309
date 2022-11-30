import socket,sys
PORT=10055
msg=""
test=""
if __name__ =="__main__":


    while msg!="kill":
        msg = ""
        server_socket = socket.socket()
        server_socket.bind(("127.0.0.1", PORT))
        server_socket.listen(5)
        print('serveur démaré')

        while msg != "kill" and msg != "reset":
            msg = ""
            conn, address = server_socket.accept()
            print("connexion")

            while msg != "disconnect" and msg != "kill"  and msg!= "reset" :
                msg = conn.recv(1024).decode()
                test = conn.send(msg.encode())
            conn.close()

        server_socket.close()

