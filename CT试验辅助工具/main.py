import sys
from run_CT import run_CT
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QRadioButton


class LoginWindow(QWidget):
    def __init__(self):
        # super().__init__()
        #
        super().__init__()
        # self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.bind()

    def bind(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginWindow()
    ex.show()
    sys.exit(app.exec_())
