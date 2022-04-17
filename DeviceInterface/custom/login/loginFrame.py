from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QPushButton, QLineEdit, QLabel

from custom.customButton import CustomButton
from webAPI.serverApi import ServerAPI


class LoginFrame(QFrame):
    login_signal = pyqtSignal(str)

    def __init__(self, parent):
        super(LoginFrame, self).__init__(parent)
        self.loginText = QLabel(self)
        self.deviceIDLineEdit = QLineEdit(self)
        self.loginButton = CustomButton(self, "Log in", 115, 135, 35)
        self.serverApi = ServerAPI()

        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #45454C;")

        # deviceIDLineEdit
        self.deviceIDLineEdit.setPlaceholderText("Device ID")
        self.deviceIDLineEdit.setGeometry(120, 410, 400, 45)
        self.deviceIDLineEdit.setFont(QFont("Arial", 15))
        self.deviceIDLineEdit.setAlignment(Qt.AlignCenter)
        self.deviceIDLineEdit.setStyleSheet("border: None; "
                                            "border-radius: 10px; "
                                            "background-color: #222226; color: white;")


        # login button
        self.loginButton.setGeometry(260, 513, 115, 35)

        # welcomeFrames label
        font = QFont("Helvetica")
        font.setWeight(30)
        font.setPixelSize(50)
        font.setBold(True)
        self.loginText.setFont(font)
        self.loginText.setText("Log in")
        self.loginText.setGeometry(215, 320, 200, 60)
        self.loginText.setAlignment(Qt.AlignCenter)
        self.loginText.setStyleSheet("color: white;")

        self.loginButton.clicked.connect(self.loginDevice)

    def loginDevice(self):
        deviceID = self.deviceIDLineEdit.text()
        if deviceID == "":
            self.deviceIDLineEdit.setStyleSheet("border: 2px solid red;")
        else:
            self.deviceIDLineEdit.setStyleSheet("border: None;")
            connected = self.serverApi.connect(deviceID)
            if connected:
                self.login_signal.emit(deviceID)
            else:
                self.deviceIDLineEdit.setStyleSheet("border: 2px solid red;")
