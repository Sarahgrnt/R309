import sys
from PyQt5.QtWidgets import *
from client import client



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
        self.__cmd= QLabel("ligne de commande:")
        self.__validecmd = QPushButton("valider")
        self.__disconnect = QPushButton("disconnect")
        self.__kill = QPushButton("validation")
        self.__reset = QPushButton("reset")
        self.__choose = QComboBox()
        self.__choose.addItem("OS")
        self.__choose.addItem("CPU")
        self.__choose.addItem("RAM")
        self.__choose.addItem("IP")
        self.__choose.addItem("Name")
        self.__commande = QComboBox()
        self.__commande.addItem( "kill")
        self.__commande.addItem("reset")
        self.__commande.addItem("disconnect")
        self.__valider = QPushButton("valider")
        self.__affichage= QTextBrowser()
        self.__choose.currentIndexChanged.connect(self.selectionchange)

        self.__valider.clicked.connect(self.traitement)
        self.__kill.clicked.connect(self.__tkt)

        grid.addWidget(self.__cmd,1,0)
        grid.addWidget(self.__textcmd,1,1)
        grid.addWidget(self.__validecmd,1,2)
        grid.addWidget(self.__choose,2,1)
        grid.addWidget(self.__valider,2,2)
        grid.addWidget(self.__affichage,2,3)
        #grid.addWidget(self.__disconnect,3,0)
        grid.addWidget(self.__kill,3,1)
        #grid.addWidget(self.__reset,3,2)
        grid.addWidget(self.__commande,3,2)


        self.setWindowTitle("Interface SAE")

    def __lireFichier(self):
        self.__affichage.setText(f"Lecture du fichier {self.__nomfichier.text()}")   # Pour debugger le code ==> code de test
        self.__clientList = []
        IP = []
        IP.append("127.0.0.1")
        #IP.append(self.__nomfichier.text())
        for ip in IP:
            self.__affichage.setText(f"Connection à {ip}")
            monclient = client(ip, 10065)
            monclient.connected()
            self.__clientList.append(monclient)
            self.__affichage.setText("connecté au serveur")

    def traitement(self,client):
        self.__temp=[]
        try:
            for client in self.__clientList:
                if self.__choose.currentText()=="OS":
                    msg=client.sended("OS")
                    self.__affichage.append(f"os: {msg}")
                if self.__choose.currentText()=="CPU":
                    msg = client.sended("CPU")
                    self.__affichage.append(f"cpu :{msg}% d'utilisation")
                if self.__choose.currentText()=="RAM":
                    msg = client.sended("RAM")
                    self.__affichage.append(f"ram: {msg}%")
                if self.__choose.currentText()=="IP":
                    msg = client.sended("IP")
                    self.__affichage.append(f"adresse ip: {msg}")
                if self.__choose.currentText()=="Name":
                    msg=client.sended("Name")
                    self.__affichage.append(f"nom du serveur:{msg}")
        except:
            self.__affichage.append("pas de serveur connecté")



    def __tkt(self):
        for client in self.__clientList:
            if self.__commande.currentText()=="kill":
                client.sended("kill")
                self.__affichage.setText("serveur mort")
            if self.__commande.currentText()=="disconnect":
                client.sended("disconnect")
                self.__affichage.setText("deconnexion")
            if self.__commande.currentText()=="reset":
                client.sended("reset")
                self.__affichage.setText("reset de la connexion")


    def selectionchange(self, i):
        print ("Items in the list are :")

        for count in range(self.__choose.count()):
            print (self.__choose.itemText(count))
        print("Current index", i, "selection changed ", self.__choose.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = interface()
    window.show()
    app.exec()