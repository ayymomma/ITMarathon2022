from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QFrame, QSizePolicy, QComboBox, QLabel, QPushButton

from customWidgets.buttons.customButton import CustomButton
from webAPI.serverApi import ServerAPI

style = """
QFrame {
    background-color: #222226;
    border-radius: 10px;
}
QComboBox{
    background-color: #45454c;
    border-radius: 10px;
    border: None;
}
"""


class ApplicationItem(QFrame):
    def __init__(self, parent=None):
        super(ApplicationItem, self).__init__(parent)
        self.versionComboBox = QComboBox(self)
        self.verticalLine = QFrame(self)
        self.applicationName = QLabel(self)
        self.updateLabel = QLabel(self)
        self.updateButton = CustomButton(self, "update", 103, 123, 28, bgColor="#5AE343", bdColor="#5AE343", color="#000000", textWeight=10, bold=False)
        self.server = ServerAPI()
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
        self.versionComboBox.setGeometry(11, 15, 159, 33)


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

        # update label
        font.setWeight(12)
        font.setPixelSize(12)
        font.setBold(True)
        self.updateLabel.setFont(font)
        self.updateLabel.setGeometry(777, 5, 143, 20)
        self.updateLabel.setStyleSheet("color: #E3B528;")
        self.updateLabel.setText("Update available")

        # update button
        self.updateButton.setGeometry(777, 26, 103, 28)
        self.updateButton.setIcon(QIcon('customWidgets/icons/Upload.png'))

    def updateData(self, name, version):
        app = self.server.getApplicationInfo(name)
        for ap in app:
            for version in ap['versions']:
                self.versionComboBox.addItem(version['versionName'])
        self.applicationName.setText(name)
        self.versionComboBox.setCurrentIndex(0)
