import socket,sys
PORT=10001
msg=""
test=""
if __name__ =="__main__":


    while True :
        server_socket = socket.socket()
        server_socket.bind(("127.0.0.1", PORT))
        server_socket.listen(1)
        print('serveur démaré')

        msg = ""
        test=""
        if msg == "kill" and test == "kill":
            conn.send("kill".encode())
            sys.exit()
        while msg != "kill" and test != "kill" and msg != "reset" and test != "reset" :
            conn, address = server_socket.accept()
            msg = ""
            test = ""


            while msg != "disconnect" and test != "disconnect" and msg != "kill" and test != "kill" and msg!= "reset" and test != "reset":
                msg = conn.recv(1024).decode()
                print(msg)
                if msg == "disconnect":
                    conn.send("disconnect".encode())
                else:
                    test = input("message:")
                    conn.send(test.encode())


            conn.close()

        server_socket.close()

