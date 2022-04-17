from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QFrame, QComboBox, QLabel, QSizePolicy

from custom.customButton import CustomButton

style = """
QFrame {
    background-color: #222226;
    border-radius: 10px;
}
#versionLabel {
    background-color: #45454c;
    border-radius: 10px;
    border: None;
}
"""


class ApplicationItem(QFrame):
    def __init__(self, parent=None):
        super(ApplicationItem, self).__init__(parent)
        self.versionLabel = QLabel(self)
        self.verticalLine = QFrame(self)
        self.applicationName = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(style)

        self.setMinimumSize(QSize(907, 64))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)
        self.setCursor(Qt.PointingHandCursor)

        # combobox
        self.versionLabel.setGeometry(11, 15, 159, 33)
        self.versionLabel.setText("Ver. 2.0.0")
        self.versionLabel.setObjectName("versionLabel")
        self.versionLabel.setAlignment(Qt.AlignCenter)

        # vertical line
        self.verticalLine.setGeometry(208, 5, 1, 55)
        self.verticalLine.setStyleSheet("background-color: #45454C;")

        # application name
        font = QFont("Helvetica")
        font.setWeight(12)
        font.setPixelSize(20)
        font.setBold(True)
        self.applicationName.setFont(font)
        self.applicationName.setGeometry(238, 12, 350, 40)
        self.applicationName.setStyleSheet("color: #FFFFFF;")
        self.applicationName.setText("Application Name")

