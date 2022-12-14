import socket
import threading
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QComboBox

PORT=10054
msg=""
data = ""
temp=[]



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
            self.__socket = socket.socket()
            print("En attente de connexion")
            self.__socket.connect((self.__hostname,self.__port))
            print("Connexion établie")

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
                temp.append(msg)
                print(msg)
            else:
                print("pas de connexion")

    #def close(self):
        #self.__socket.close()

 class interface(QMainWindow):
        def __init__(self):
            super().__init__()
            widget = QWidget()
            self.setCentralWidget(widget)
            grid = QGridLayout()
            widget.setLayout(grid)
            self.__fichier = QLabel("Lecture de fichier")
            self.__nomfichier = QLineEdit("")
            self.__lire = QPushButton("Lire")

            grid.addWidget(self.__fichier, 0, 0)
            grid.addWidget(self.__nomfichier, 0, 1)
            grid.addWidget(self.__lire, 0, 2)

            self.__lire.clicked.connect(self.__lireFichier)

            self.__textcmd = QLineEdit("")
            self.__cmd = QLabel("ligne de commande:")
            self.__validecmd = QPushButton("valider")
            self.__disconnect = QPushButton("disconnect")
            self.__kill = QPushButton("kill")
            self.__reset = QPushButton("reset")
            self.__choose = QComboBox()
            self.__choose.addItem("OS")
            self.__choose.addItem("CPU")
            self.__choose.addItem("RAM")
            self.__choose.addItem("IP")
            self.__choose.addItem("Name")
            self.__commande = QComboBox()
            self.__commande.addItem("kill")
            self.__commande.addItem("reset")
            self.__commande.addItem("disconnect")
            self.__valider = QPushButton("valider1")
            self.__affichage = QLineEdit("")
            self.__choose.currentIndexChanged.connect(self.selectionchange)

            self.__valider.clicked.connect(self.__traitement)
            self.__kill.clicked.connect(self.__tkt)

            grid.addWidget(self.__cmd, 1, 0)
            grid.addWidget(self.__textcmd, 1, 1)
            grid.addWidget(self.__validecmd, 1, 2)
            grid.addWidget(self.__choose, 2, 1)
            grid.addWidget(self.__valider, 2, 2)
            grid.addWidget(self.__affichage, 2, 3)
            grid.addWidget(self.__disconnect, 3, 0)
            grid.addWidget(self.__kill, 3, 1)
            grid.addWidget(self.__reset, 3, 2)
            grid.addWidget(self.__commande, 4, 1)

            self.setWindowTitle("Interface SAE")

        def __lireFichier(self):
            print(f"Lecture du fichier {self.__nomfichier.text()}")
            # Pour debugger le code ==> code de test
            self.__clientList = []
            IP = []
            IP.append("localhost")
            # IP.append(self.__nomfichier.text())
            for ip in IP:
                print(f"Connection à {ip}")
                monclient = client(ip, 10054)
                monclient.connected()
                self.__clientList.append(monclient)

        def __traitement(self):
            for client in self.__clientList:
                if self.__choose.currentText() == "OS":
                    client.sended("OS")
                    self.__affichage== temp
                print("messge envoyé")
                if self.__choose.currentText() == "CPU":
                    client.sended("CPU")
                    print("message envoyé")
                if self.__choose.currentText() == "RAM":
                    client.sended("RAM")
                    print("message envoyé")
                if self.__choose.currentText() == "IP":
                    client.sended("IP")
                    print("message envoyé")
                if self.__choose.currentText() == "Name":
                    client.sended("Name")
                    print("message envoyé")

        def __tkt(self):
            for client in self.__clientList:
                if self.__commande.currentText() == "kill":
                    client.sended("kill")
                    print("close")
                    client.close()
                if self.__commande.currentText() == "disconnect":
                    client.sended("disconnect")
                    client.close()
                if self.__commande.currentText() == "reset":
                    client.sended("reset")
                    client.close()

        def selectionchange(self, i):
            print("Items in the list are :")

            for count in range(self.__choose.count()):
                print(self.__choose.itemText(count))
            print("Current index", i, "selection changed ", self.__choose.currentText())


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

    app = QApplication(sys.argv)
    window = interface()
    window.show()
    app.exec()

