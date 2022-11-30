import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QComboBox

class interface(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.__fichier = QLabel("Lecture de fichier")
        self.__ajout = QPushButton("ajouter des machines")
        self.__nom = QLabel("nom:")
        self.__textnom= QLineEdit("")
        self.__ip = QLabel("ip:")
        self.__textip = QLineEdit("")
        self.__os = QLabel("os:")
        self.__textos = QLineEdit("")
        self.__ram = QLabel("ram:")
        self.__textram = QLineEdit("")
        self.__cpu = QLabel("nom:")
        self.__textcpu = QLineEdit("")
        self.__choose = QComboBox()
        self.__choose.addItem("test")
        self.__valider = QPushButton("valider")
        self.__choose.currentIndexChanged.connect(self.selectionchange)


        grid.addWidget(self.__fichier,0,0)
        grid.addWidget(self.__ajout,1,0)
        grid.addWidget(self.__choose,2,0)
        grid.addWidget(self.__valider,2,1)

        #self.__valider.clicked.connect()
        self.setWindowTitle("Interface SAE")


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