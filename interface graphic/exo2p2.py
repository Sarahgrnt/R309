from PyQt5.QtWidgets import *
import sys


class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        lab = QLabel("Permet de convertir des températures en Celsius et Kelvin")

        # Constructeur
        self.__lab = lab

        # Affichage
        grid.addWidget(self.__lab, 0, 0)

        self.setWindowTitle("Aide")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow2()
    window.show()
    app.exec()
