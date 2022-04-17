from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QFrame, QLabel, QPushButton

from customWidgets.buttons.customButton import CustomButton
from customWidgets.userFrames.applicationsFrame import ApplicationsFrame
from customWidgets.userFrames.devicesFrame import DevicesFrame

style = """
QFrame {
    background-color: #171719;
}
QLabel {
    color: #FFFFFF;
}
"""


class UserFrame(QFrame):
    def __init__(self, parent):
        super(UserFrame, self).__init__(parent)
        self.welcomeLabel = QLabel(self)
        self.devicesFrame = DevicesFrame(self)
        self.applicationsFrame = ApplicationsFrame(self)
        self.addDeviceButton = CustomButton(self, "", 218, 238, 43)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(style)
        self.setGeometry(0, 0, 1350, 900)

        font = QFont("Helvetica")
        font.setWeight(20)
        font.setPixelSize(30)
        font.setBold(True)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setText("Welcome, user!")
        self.welcomeLabel.setGeometry(90, 25, 300, 30)

        self.addDeviceButton.setGeometry(116, 825, 218, 43)
        self.addDeviceButton.setText("Add new device")
        self.addDeviceButton.setStyleSheet("background-color: #5AE343;"
                                           "color: black;"
                                           "border-radius: 20px;"
                                           "style: flat;")
        self.addDeviceButton.setIcon(QIcon('customWidgets/icons/plus.png'))
        self.addDeviceButton.setIconSize(QSize(30, 30))
        font.setBold(False)
        font.setWeight(10)
        font.setPixelSize(20)
        self.addDeviceButton.setFont(font)

