from PyQt5.QtWidgets import QFrame, QPushButton

from customFrames.login.loginFrame import LoginFrame
from customFrames.login.registerFrame import RegisterFrame


class LoginOrRegisterFrame(QFrame):

    def __init__(self, parent):
        super(LoginOrRegisterFrame, self).__init__(parent)
        self.loginButton = QPushButton(self)
        self.registerButton = QPushButton(self)
        self.loginFrame = LoginFrame(parent)
        self.registerFrame = RegisterFrame(parent)
        self.initUI()

    def initUI(self):
        # log in button
        self.loginButton.setText("Log in")
        self.loginButton.setGeometry(70, 370, 480, 60)
        self.loginButton.clicked.connect(self.showLoginFrame)

        # register button
        self.registerButton.setText("Register")
        self.registerButton.setGeometry(70, 470, 480, 60)
        self.registerButton.clicked.connect(self.showRegisterFrame)

        # login frame
        self.loginFrame.hide()
        self.loginFrame.setGeometry(715, 0, 635, 900)

        # register frame
        self.registerFrame.hide()
        self.registerFrame.setGeometry(715, 0, 635, 900)

    def showLoginFrame(self):
        self.loginFrame.show()
        self.hide()

    def showRegisterFrame(self):
        self.registerFrame.show()
        self.hide()
