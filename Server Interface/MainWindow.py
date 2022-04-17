import os
import sys

import psutil
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from customWidgets.userFrames.userFrame import UserFrame
from customWidgets.welcomeFrames.welcomeFrame import WelcomeFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.centralWidget = QtWidgets.QWidget(self)
        self.welcomeFrame = WelcomeFrame(self.centralWidget)
        self.userFrame = UserFrame(self.centralWidget)
        self.setCentralWidget(self.centralWidget)



        self.initUI()

    def initUI(self):
        self.setWindowTitle("ITMarathon")
        self.resize(1350, 900)
        self.setMinimumSize(1350, 900)
        self.setMaximumSize(1350, 900)

        # user frame
        self.userFrame.hide()

        # welcome frame
        self.welcomeFrame.loginOrRegisterFrame.loginFrame.loginButton.clicked.connect(self.login)

    def login(self):
        self.welcomeFrame.hide()
        self.userFrame.show()


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    if including_parent:
        parent.kill()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wifiTest = MainWindow()
    wifiTest.show()
    returnValue = app.exec()
    if returnValue is not None:
        kill_proc_tree(os.getpid())
        sys.exit(returnValue)
