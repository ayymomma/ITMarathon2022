from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

from customWidgets.adminFrames.applicationItem import ApplicationItem
from customWidgets.adminFrames.applicationsFrame import ApplicationsFrame
from webAPI.serverApi import ServerAPI

style = """
QFrame {
    background-color: #171719;
}
QLabel {
    color: #FFFFFF;
}
"""


class AdminFrame(QFrame):

    def __init__(self, parent):
        super(AdminFrame, self).__init__(parent)
        self.welcomeLabel = QLabel(self)
        self.applicationFrame = ApplicationsFrame(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1350, 900)
        self.setStyleSheet(style)

        font = QFont("Helvetica")
        font.setWeight(20)
        font.setPixelSize(30)
        font.setBold(True)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setText("Welcome!")
        self.welcomeLabel.setGeometry(90, 25, 300, 30)

        self.applicationFrame.addItem(ApplicationItem())
        self.applicationFrame.addItem(ApplicationItem())
        self.applicationFrame.addItem(ApplicationItem())
