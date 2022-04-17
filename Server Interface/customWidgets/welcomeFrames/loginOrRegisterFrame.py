from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QPushButton, QLabel

from customWidgets.buttons.customButton import CustomButton
from customWidgets.welcomeFrames.loginFrame import LoginFrame
from customWidgets.welcomeFrames.registerFrame import RegisterFrame


class LoginOrRegisterFrame(QFrame):

    def __init__(self, parent):
        super(LoginOrRegisterFrame, self).__init__(parent)
        self.loginButton = CustomButton(self, "Log in", 480, 500, 60)
        self.registerButton = CustomButton(self, "Register", 480, 500, 60)
        self.welcomeLabel = QLabel(self)
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

        # welcomeFrames frame
        self.loginFrame.hide()
        self.loginFrame.setGeometry(715, 0, 635, 900)
        self.loginFrame.backButton.clicked.connect(self.hideLoginFrame)

        # register frame
        self.registerFrame.hide()
        self.registerFrame.setGeometry(715, 0, 635, 900)
        self.registerFrame.backButton.clicked.connect(self.hideRegisterFrame)

        # welcome label
        font = QFont("Helvetica")
        font.setWeight(30)
        font.setPixelSize(50)
        font.setBold(True)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setText("WELCOME!")
        self.welcomeLabel.setGeometry(170, 230, 300, 60)

    def showLoginFrame(self):
        self.loginFrame.show()
        self.hide()

    def showRegisterFrame(self):
        self.registerFrame.show()
        self.hide()

    def hideLoginFrame(self):
        self.loginFrame.hide()
        self.show()

    def hideRegisterFrame(self):
        self.registerFrame.hide()
        self.show()
