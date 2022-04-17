from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

from custom.aplication.applicationFrame import ApplicationsFrame
from custom.aplication.applicationItem import ApplicationItem
from deviceDataReader import DeviceDataReader
from webAPI.serverApi import ServerAPI

style = """
QFrame {
    background-color: #171719;
}
QLabel {
    color: #FFFFFF;
}
"""


class DeviceFrame(QFrame):

    def __init__(self, parent):
        super(DeviceFrame, self).__init__(parent)
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

        print(DeviceDataReader.get_applications())
        for appData in DeviceDataReader.get_applications():
            app = ApplicationItem(appData=appData)
            self.applicationFrame.addItem(app)

    def show(self) -> None:
        super(DeviceFrame, self).show()
        self.welcomeLabel.setText("Welcome, " + ServerAPI.get_device_name()+"!")