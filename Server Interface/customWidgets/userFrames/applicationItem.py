from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QFrame, QSizePolicy

style = """
QFrame {
    background-color: #222226;
    border-radius: 10px;
}
"""


class ApplicationItem(QFrame):
    def __init__(self, parent=None):
        super(ApplicationItem, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(style)

        self.setMinimumSize(QSize(907, 64))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)
        self.setCursor(Qt.PointingHandCursor)
