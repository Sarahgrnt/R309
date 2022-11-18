import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QComboBox
from exo2p2 import MainWindow2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.__lab = QLabel("température")
        self.__texttemp = QLineEdit("")
        self.__labc = QLabel("°C")
        self.__convertir = QPushButton("convertir")
        self.__Kelvin = QLabel("Kelvin")
        self.__textK = QLineEdit("")
        self.__labK = QLabel("°K")
        self.__box = QComboBox()
        self.__box.addItem("C -> K")
        self.__box.addItem("K -> C")
        self.__calc = QLineEdit("")
        self.__aide = QPushButton("?")
        self.__box.currentIndexChanged.connect(self.selectionchange)
        # Ajouter les composants au grid ayout
        grid.addWidget(self.__lab, 0, 0)
        grid.addWidget(self.__texttemp,0,1)
        grid.addWidget(self.__labc,0,2)
        grid.addWidget(self.__convertir,1,1)
        grid.addWidget(self.__Kelvin,2,0)
        grid.addWidget(self.__textK,2,1)
        grid.addWidget(self.__labK,2,2)
        grid.addWidget(self.__box,1,2)
        grid.addWidget(self.__aide,2,3)
        self.__convertir.clicked.connect(self._Convertion)
        self.__aide.clicked.connect(self._actionAide)
        self.setWindowTitle("Conversion de température")

    def selectionchange(self, i):
        print ("Items in the list are :")

        for count in range(self.__box.count()):
            print (self.__box.itemText(count))
        print("Current index", i, "selection changed ", self.__box.currentText())

    def _Convertion(self):
        if self.__box.currentText() =="C -> K":
            try:
                temp = float(self.__texttemp.text()) + 273.15
                self.__textK.setText(f"{temp}")
            except ValueError:
                print('Mettre des chiffres')
        else:
            try:
                temp = float(self.__textK.text()) - 273.15
                self.__texttemp.setText(f"{temp}")
            except ValueError:
                print('Mettre des chiffres')

    def _actionQuitter(self):
        QCoreApplication.exit(0)

    def _actionAide(self):
        self.__aide = MainWindow2()
        self.__aide.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
