from PyQt5 import QtGui
from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QLabel

from webAPI.serverApi import ServerAPI

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
    add_apps_signal = pyqtSignal(list)

    def __init__(self, parent=None):
        super(DeviceItem, self).__init__(parent)
        self.deviceName = QLabel(self)
        self.deviceID = ""
        self.appList = []
        self.server = ServerAPI()
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

    def mouseReleaseEvent(self, e):
        super(DeviceItem, self).mouseReleaseEvent(e)
        apps = self.server.getApplicationsForDevice(self.deviceID)
        print(apps)
        self.add_apps_signal.emit(apps)

