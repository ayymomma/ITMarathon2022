import os
import sys

import psutil
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from customWidgets.adminFrames.adminFrame import AdminFrame
from customWidgets.userFrames.userFrame import UserFrame
from customWidgets.welcomeFrames.welcomeFrame import WelcomeFrame
from webAPI.serverApi import ServerAPI


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.centralWidget = QtWidgets.QWidget(self)
        self.welcomeFrame = WelcomeFrame(self.centralWidget)
        self.userFrame = UserFrame(self.centralWidget)
        self.adminFrame = AdminFrame(self.centralWidget)
        self.server = ServerAPI()
        self.setCentralWidget(self.centralWidget)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("ITMarathon")
        self.resize(1350, 900)
        self.setMinimumSize(1350, 900)
        self.setMaximumSize(1350, 900)

        # user frame
        self.userFrame.hide()
        self.adminFrame.hide()

        # welcome frame
        self.welcomeFrame.loginOrRegisterFrame.loginFrame.login_signal.connect(self.login)

    def login(self, role):
        if role == "ADMIN":
            self.welcomeFrame.hide()
            self.adminFrame.welcomeLabel.setText(f'Welcome, {self.server.user}!')
            self.adminFrame.show()
        elif role == "USER":
            self.welcomeFrame.hide()
            self.adminFrame.welcomeLabel.setText(f'Welcome, {self.server.user}!')
            self.userFrame.show()



def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    if including_parent:
        parent.kill()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    itMarathon = MainWindow()
    itMarathon.show()
    returnValue = app.exec()
    if returnValue is not None:
        kill_proc_tree(os.getpid())
        sys.exit(returnValue)
