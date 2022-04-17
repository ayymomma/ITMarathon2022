from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

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

