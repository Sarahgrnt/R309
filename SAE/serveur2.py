import socket,sys,os
PORT=10055
msg=""
test=""
cmd=""
if __name__ =="__main__":


    while msg!="kill":
        msg = ""
        cmd=""
        server_socket = socket.socket()
        server_socket.bind(("127.0.0.1", PORT))
        server_socket.listen(5)
        print('serveur démaré')

        while msg != "kill" and msg != "reset":
            msg = ""
            cmd=""
            conn, address = server_socket.accept()
            print("connexion")
            if cmd == "ip" or "IP":
                conn.send((socket.gethostbyname(socket.gethostname())).encode())
            if cmd == "name" or "Name":
                conn.send((socket.gethostname()).encode())

            while msg != "disconnect" and msg != "kill"  and msg!= "reset" :
                msg = conn.recv(1024).decode()
                test = conn.send(msg.encode())



            conn.close()

        server_socket.close()

