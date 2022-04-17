from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QLabel, QLineEdit, QPushButton


class RegisterFrame(QFrame):

    def __init__(self, parent):
        super(RegisterFrame, self).__init__(parent)
        self.registerText = QLabel(self)
        self.usernameLineEdit = QLineEdit(self)
        self.passwordLineEdit = QLineEdit(self)
        self.repeatPasswordLineEdit = QLineEdit(self)
        self.registerButton = QPushButton(self)
        self.initUI()

    def initUI(self):
        # username line edit
        self.usernameLineEdit.setPlaceholderText("Username")
        self.usernameLineEdit.setGeometry(120, 340, 400, 45)

        # password line edit
        self.passwordLineEdit.setPlaceholderText("Password")
        self.passwordLineEdit.setGeometry(120, 430, 400, 45)

        # repeat password line edit
        self.repeatPasswordLineEdit.setPlaceholderText("Repeat password")
        self.repeatPasswordLineEdit.setGeometry(120, 490, 400, 45)

        # login button
        self.registerButton.setGeometry(260, 640, 115, 35)
        self.registerButton.setText("Register")

        # login label
        self.registerText.setGeometry(215, 260, 200, 50)
        self.registerText.setAlignment(Qt.AlignCenter)
        self.registerText.setText("REGISTER")
