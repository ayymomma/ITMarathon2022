from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

from customWidgets.userFrames.deviceItem import DeviceItem
from customWidgets.userFrames.scrollAreaDevices import ScrollAreaDevices

style = """
QFrame {
background-color: #2e2e33;
border-radius: 15px;
border: 2px;
}
"""


class DevicesFrame(QFrame):
    def __init__(self, parent):
        super(DevicesFrame, self).__init__(parent)
        self.deviceTitle = QLabel(self)
        self.scrollAreaDevices = ScrollAreaDevices(self)

        self.initUI()

    def initUI(self):
        self.setGeometry(55, 97, 345, 788)
        self.setStyleSheet(style)

        font = QFont("Helvetica")
        font.setWeight(12)
        font.setPixelSize(20)
        font.setBold(True)
        self.deviceTitle.setFont(font)
        self.deviceTitle.setText("Devices")
        self.deviceTitle.setGeometry(64, 15, 200, 30)
        self.deviceTitle.setAlignment(Qt.AlignCenter)

        self.scrollAreaDevices.addWidget(DeviceItem())
        self.scrollAreaDevices.addWidget(DeviceItem())
        self.scrollAreaDevices.addWidget(DeviceItem())
        self.scrollAreaDevices.addWidget(DeviceItem())
