import socket,sys
import psutil
PORT=10065
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

        while msg != "kill" and msg != "reset" :
            msg = ""
            conn, address = server_socket.accept()
            print("connexion")

            while msg != "disconnect" and msg != "kill" and msg != "reset":
                msg = conn.recv(1024).decode()
                if msg == "IP":
                    msg =socket.gethostbyname(socket.gethostname())
                    conn.send(msg.encode())
                elif msg == "Name":
                    msg = socket.gethostname()
                    conn.send(msg.encode())
                elif msg == "CPU":
                    msg = str(psutil.cpu_percent())
                    conn.send(msg.encode())
                elif msg == "RAM":
                    psutil.virtual_memory()  # you can convert that object to a dictionary dict
                    psutil.virtual_memory()._asdict()
                    msg = str(psutil.virtual_memory().percent)
                    conn.send(msg.encode())
                elif msg == "OS":
                    msg = str(sys.platform)
                    conn.send(msg.encode())
                    print(msg)

                elif msg == "python":
                    msg = str(sys.version)
                    conn.send(msg.encode())
                else:
                    conn.send(msg.encode())
            conn.close()

        server_socket.close()

