from PyQt5.QtWidgets import QFrame

from custom.login.loginFrame import LoginFrame


class LoginOrRegisterFrame(QFrame):

    def __init__(self, parent):
        super(LoginOrRegisterFrame, self).__init__(parent)
        self.loginFrame = LoginFrame(self)
        self.initUI()

    def initUI(self):
        self.loginFrame.setGeometry(715, 0, 635, 900)


