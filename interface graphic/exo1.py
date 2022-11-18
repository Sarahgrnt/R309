import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        lab = QLabel("Saisir votre nom")
        self.__text = QLineEdit("")
        self.__bonjour = QLabel("")
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")
        # Ajouter les composants au grid ayout
        grid.addWidget(lab, 0, 0)
        grid.addWidget(self.__text,1,0)
        grid.addWidget(self.__bonjour,3,0)
        grid.addWidget(ok,2,0)
        grid.addWidget(quit,4,0)
        ok.clicked.connect(self._actionOk)
        quit.clicked.connect(self._actionQuitter)
        self.setWindowTitle("Une première fenêtre")

    def _actionOk(self):
        self.__bonjour.setText(f"Bonjour {self.__text.text()}")

    def _actionQuitter(self):
        QCoreApplication.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
