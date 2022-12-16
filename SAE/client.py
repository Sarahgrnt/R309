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

    def connect(self):#faire une connection threader
        self.tConnected = threading.Thread(target=self.connected)
        self.tConnected.start()

    def connected(self):
            self.__socket = socket.socket()
            print("En attente de connexion")
            self.__socket.connect((self.__hostname,self.__port))
            print("Connexion établie")

    def send(self, msg):#envoie de message pour thread
        self.verrou = threading.Lock()
        self.verrou.acquire()
        self.tSend = threading.Thread(target=self.sended, args=[msg])
        self.tSend.start()
        self.verrou.release()

    def waitSend(self):
        self.tSend.join()

    def sended(self,msg):
            if self.isConnected():
                while msg != "disconnect" and msg != "kill" and msg != "reset":
                    self.__socket.send(msg.encode())
                    msg = self.__socket.recv(1024).decode()
                    #print(f"{msg} message client")
                    return msg
                self.__socket.close()
            else:
                 print("pas de connexion")

    def close(self):
        self.__socket.close()

    def receive(self):
        msg = self.__socket.recv(1024).decode()
        print(f"{msg} message client1")

    def data(self,msg):
        try:
            while msg != "disconnect" and msg != "kill":
                msg = ""
                client_socket = socket.socket()
                client_socket.connect(("127.0.0.1", PORT))
                print("connecté au serveur")

                while msg != "disconnect" and msg != "kill" and msg != "reset":
                    client_socket.send(msg.encode())
                    data = client_socket.recv(1024).decode()
                    print(data)

                client_socket.close()
        except ConnectionError:
            print("pas de serveur")


#if __name__ =="__main__":





