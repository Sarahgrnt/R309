import socket,sys,os
import os
import psutil

import resp as resp
from ping3 import ping
PORT=10056
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
            #conn.send(socket.gethostbyname(socket.gethostname()).encode())
            #conn.send(socket.gethostname().encode())

            while msg != "disconnect" and msg != "kill"  and msg!= "reset":
                msg = conn.recv(1024).decode()
                if msg == "ip":
                    msg = socket.gethostbyname(socket.gethostname())
                    conn.send(msg.encode())
                elif msg == "name":
                    msg= socket.gethostname()
                    conn.send(msg.encode())
                elif msg== "cpu":
                    msg=str(psutil.cpu_percent())
                    conn.send(msg.encode())
                elif msg == "RAM":
                    psutil.virtual_memory()  # you can convert that object to a dictionary dict
                    (psutil.virtual_memory()._asdict())
                    msg=str(psutil.virtual_memory().percent)
                    conn.send(msg.encode())
                elif msg == "OS":
                    conn.send(sys.platform.encode())
                else:
                    conn.send(msg.encode())
            conn.close()

        server_socket.close()

