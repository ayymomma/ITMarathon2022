import os
import sys

import psutil
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from custom.aplication.applicationItem import ApplicationItem
from custom.aplication.deviceFrame import DeviceFrame
from custom.login.loginDevice import LoginOrRegisterFrame
from deviceDataReader import DeviceDataReader

style = """
QMainWindow {
    background-color: #171719;
}
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.centralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.deviceDataReader = DeviceDataReader()
        self.deviceData = self.deviceDataReader.read()

        self.deviceFrame = DeviceFrame(self.centralWidget)
        self.loginFrame = LoginOrRegisterFrame(self.centralWidget)

        self.setCentralWidget(self.centralWidget)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("ITMarathon")
        self.resize(1350, 900)
        self.setMinimumSize(1350, 900)
        self.setMaximumSize(1350, 900)
        self.setStyleSheet(style)

        self.loginFrame.loginFrame.login_signal.connect(self.login)

        self.deviceFrame.hide()

    def login(self, device_id):
        self.deviceFrame.show()
        self.loginFrame.hide()


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
