import sys
#lien github https://github.com/Sarahgrnt/R309/tree/sarah.grenot%40uha.fr/examen
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QComboBox
from clientexam import connected

class interface(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.__serveur=QLabel("Serveur")
        self.__serveurline=QLineEdit("localhost")
        self.__port= QLabel("Port")
        self.__portline=QLineEdit("10058")
        self.__connexion = QPushButton("Connexion")

        grid.addWidget(self.__serveur,0,0)
        grid.addWidget(self.__serveurline,0,1)
        grid.addWidget(self.__port,1,0)
        grid.addWidget(self.__portline,1,1)
        grid.addWidget(self.__connexion,2,1)

        self.__connexion.clicked.connect(self.jesaispas)

        self.__text=QLineEdit("")

        grid.addWidget(self.__text,3,0)

        self.__messsage=QLabel("Message:")
        self.__textmessage= QLineEdit("")
        self.__envoyer = QPushButton("Envoyer")

        grid.addWidget(self.__messsage,4,0)
        grid.addWidget(self.__textmessage,4,1)
        grid.addWidget(self.__envoyer,5,0)

        self.__effacer=QPushButton("Effacer")
        self.__quitter= QPushButton("Quitter")

        grid.addWidget(self.__effacer,6,0)
        grid.addWidget(self.__quitter,6,1)

        self.__effacer.clicked.connect(self.effacer)

        self.setWindowTitle("Un logiciel de tchat")



    def jesaispas(self):
        self.__clientList = []
        IP = []
        IP.append("localhost")
        for ip in IP:
            print(f"Connection à {ip}")
            monclient = connected(ip, 10058)
            monclient.connected()
            print("connecté au serveur")

    def effacer(self):
           self.__textmessage =""

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = interface()
    window.show()
    app.exec()