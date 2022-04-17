from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QFrame, QComboBox, QLabel, QSizePolicy

from customWidgets.buttons.customButton import CustomButton

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
        self.uploadButton = CustomButton(self, "upload", 103, 123, 28, bgColor="#5AE343", bdColor="#5AE343", color="#000000", textWeight=10, bold=False)
        self.deleteButton = CustomButton(self, "remove", 103, 123, 28, bgColor="#e34343", bdColor="#e34343", color="#000000", textWeight=10, bold=False)
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
        self.versionComboBox.addItem("1.2.0")
        self.versionComboBox.addItem("1.3.0")
        self.versionComboBox.addItem("1.4.0")

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

        # update button
        self.uploadButton.setGeometry(1103, 16, 119, 32)
        self.uploadButton.setIcon(QIcon('customWidgets/icons/Upload.png'))

        # delete button
        self.deleteButton.setGeometry(973, 16, 119, 32)
        self.deleteButton.setIcon(QIcon('customWidgets/icons/Trash.png'))
