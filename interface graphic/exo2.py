import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QComboBox


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
        self.__convertir.clicked.connect(self._Convertion)
        self.setWindowTitle("Conversion de température")

    def selectionchange(self, i):
        print ("Items in the list are :")

        for count in range(self.__box.count()):
            print (self.__box.itemText(count))
        print("Current index", i, "selection changed ", self.__box.currentText())

    def _Convertion(self):
        if self.__box.currentText() =="C -> K":
            temp = float(self.__texttemp.text()) + 273.15
            self.__textK.setText(f"{temp}")
        else:
            temp = float(self.__textK.text()) - 273.15
            self.__texttemp.setText(f"{temp}")

    def _actionQuitter(self):
        QCoreApplication.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
