from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QPushButton, QLineEdit, QLabel

from customWidgets.buttons.customButton import CustomButton


class LoginFrame(QFrame):
    def __init__(self, parent):
        super(LoginFrame, self).__init__(parent)
        self.loginText = QLabel(self)
        self.usernameLineEdit = QLineEdit(self)
        self.passwordLineEdit = QLineEdit(self)
        self.loginButton = CustomButton(self, "Log in", 115, 135, 35)
        self.backButton = CustomButton(self, "Back", 115, 135, 35)
        self.initUI()

    def initUI(self):
        # username line edit
        self.usernameLineEdit.setPlaceholderText("Username")
        self.usernameLineEdit.setGeometry(120, 410, 400, 45)

        # password line edit
        self.passwordLineEdit.setPlaceholderText("Password")
        self.passwordLineEdit.setGeometry(120, 470, 400, 45)

        # login button
        self.loginButton.setGeometry(180, 600, 115, 35)

        # back button
        self.backButton.setGeometry(350, 600, 115, 35)

        # welcomeFrames label
        font = QFont("Helvetica")
        font.setWeight(30)
        font.setPixelSize(50)
        font.setBold(True)
        self.loginText.setFont(font)
        self.loginText.setText("Log in")
        self.loginText.setGeometry(215, 320, 200, 60)
        self.loginText.setAlignment(Qt.AlignCenter)

