from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QPushButton, QSizePolicy

style = """
QPushButton {
    background-color: #222226;
    border-radius: 10px;
}
"""


class DeviceItem(QPushButton):

    def __init__(self, parent=None):
        super(DeviceItem, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(style)

        self.setMinimumSize(QSize(301, 58))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)
        self.setCursor(Qt.PointingHandCursor)
