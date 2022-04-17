from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QFrame, QComboBox, QLabel, QSizePolicy

from customWidgets.adminFrames.newVersionDialog import NewVersionDialog
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
        self.newVersionDialog = None
        self.versionComboBox = QComboBox(self)
        self.verticalLine = QFrame(self)
        self.applicationName = QLabel(self)
        self.uploadButton = CustomButton(self, "upload", 103, 123, 28, bgColor="#5AE343", bdColor="#5AE343", color="#000000", textWeight=10, bold=False)
        self.deleteButton = CustomButton(self, "remove", 103, 123, 28, bgColor="#e34343", bdColor="#e34343", color="#000000", textWeight=10, bold=False)
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

        # update button
        self.uploadButton.setGeometry(1103, 16, 119, 32)
        self.uploadButton.setIcon(QIcon('customWidgets/icons/Upload.png'))
        self.uploadButton.clicked.connect(self.openNewVersionDialog)

        # delete button
        self.deleteButton.setGeometry(973, 16, 119, 32)
        self.deleteButton.setIcon(QIcon('customWidgets/icons/Trash.png'))

    def setName(self, name):
        self.applicationName.setText(name)

    def setVersion(self, version):
        for vers in version:
            self.versionComboBox.addItem(vers['versionName'])

    def openNewVersionDialog(self):
        self.newVersionDialog = NewVersionDialog(self)
        self.newVersionDialog.show()
        self.newVersionDialog.add_vers_signal.connect(self.addVers)

    def addVers(self, vers, path):
        if self.server.addNewVersion(self.applicationName.text(), vers, path):
            self.versionComboBox.addItem(vers)
        self.newVersionDialog.hide()
        self.newVersionDialog = None
