from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

from custom.customButton import CustomButton
from custom.loginFrame import LoginFrame


class LoginOrRegisterFrame(QFrame):

    def __init__(self, parent):
        super(LoginOrRegisterFrame, self).__init__(parent)
        self.loginFrame = LoginFrame(parent)
        self.initUI()

    def initUI(self):
        self.loginFrame.setGeometry(715, 0, 635, 900)


