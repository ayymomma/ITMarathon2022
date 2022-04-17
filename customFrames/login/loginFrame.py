from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QPushButton, QLineEdit, QLabel


class LoginFrame(QFrame):
    def __init__(self, parent):
        super(LoginFrame, self).__init__(parent)
        self.loginText = QLabel(self)
        self.usernameLineEdit = QLineEdit(self)
        self.passwordLineEdit = QLineEdit(self)
        self.loginButton = QPushButton(self)
        self.initUI()

    def initUI(self):
        # username line edit
        self.usernameLineEdit.setPlaceholderText("Username")
        self.usernameLineEdit.setGeometry(120, 410, 400, 45)

        # password line edit
        self.passwordLineEdit.setPlaceholderText("Password")
        self.passwordLineEdit.setGeometry(120, 470, 400, 45)

        # login button
        self.loginButton.setGeometry(260, 600, 115, 35)
        self.loginButton.setText("Log in")

        # login label
        self.loginText.setGeometry(215, 335, 200, 50)
        self.loginText.setAlignment(Qt.AlignCenter)
        self.loginText.setText("LOG IN")

