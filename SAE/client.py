import socket
import threading
PORT=10054
msg=""
data = ""


class client():
    def __init__(self, hostname=int, port=int):
        self.__port = port
        self.__hostname = hostname
        self.__socket = None

    def isConnected(self):
        return (self.__socket != None)

    def connect(self):
        self.tConnected = threading.Thread(target=self.connected)
        self.tConnected.start()

    def connected(self):
        try:
            self.__socket = socket.socket()
            print("En attente de connexion")
            self.__socket.connect((self.__hostname,self.__port))
            print("Connexion établie")
        except BrokenPipeError:
            print("serveur non connecté")

    def send(self, msg):
        self.verrou = threading.Lock()
        self.verrou.acquire()
        self.tSend = threading.Thread(target=self.sended, args=[msg])
        self.tSend.start()
        self.verrou.release()

    def waitSend(self):
        self.tSend.join()

    def sended(self,msg):
        if self.isConnected():
            self.__socket.send(msg.encode())
            msg= self.__socket.recv(1024).decode()
            print(msg)
        else:
            print("pas de connexion")




    def close(self):
        self.__socket.close()

if __name__ =="__main__":

    try:
        while msg != "disconnect" and msg != "kill":
            msg = ""
            client_socket = socket.socket()
            client_socket.connect(("127.0.0.1", PORT))
            print("connecté au serveur")

            while msg != "disconnect" and msg != "kill" and msg != "reset":
                msg = str(input("message:"))
                envoie = client_socket.send(msg.encode())
                data = client_socket.recv(1024).decode()
                print(data)

            client_socket.close()
    except ConnectionError:
        print("pas de serveur")



