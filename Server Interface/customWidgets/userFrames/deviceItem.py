from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QLabel

style = """
QPushButton {
    background-color: #222226;
    border-radius: 10px;
}
QLabel {
    color: #ffffff;
    background-color: #222226;
}
"""


class DeviceItem(QPushButton):

    def __init__(self, parent=None):
        super(DeviceItem, self).__init__(parent)
        self.deviceName = QLabel(self)
        self.deviceID = ""
        self.appList = []
        self.initUI()

    def initUI(self):
        self.setStyleSheet(style)

        self.setMinimumSize(QSize(301, 58))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)
        self.setCursor(Qt.PointingHandCursor)

        # deviceName
        font = QFont("Helvetica")
        font.setWeight(15)
        font.setPixelSize(20)
        font.setBold(True)
        self.deviceName.setFont(font)
        self.deviceName.setGeometry(46, 14, 237, 29)
        self.deviceName.setAlignment(Qt.AlignCenter)
        self.deviceName.setText("Device Name")

    def setName(self, text):
        self.deviceName.setText(text)

    def setDeviceId(self, id):
        self.deviceID = id
