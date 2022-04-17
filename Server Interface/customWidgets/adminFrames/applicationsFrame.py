from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QFrame, QLabel

from customWidgets.adminFrames.newAppDialog import NewAppDialog
from customWidgets.buttons.customButton import CustomButton
from customWidgets.userFrames.applicationItem import ApplicationItem
from customWidgets.userFrames.scrollAreaApplications import ScrollAreaApplications
from webAPI.serverApi import ServerAPI

style = """
QFrame {
    background-color: #2e2e33;
    border-radius: 10px;
}
"""


class ApplicationsFrame(QFrame):
    def __init__(self, parent):
        super(ApplicationsFrame, self).__init__(parent)
        self.newAppDialog = None
        self.applicationTitle = QLabel(self)
        self.scrollAreaApplications = ScrollAreaApplications(self)
        self.addAppButton = CustomButton(self, "", 164, 184, 33)
        self.itemList = []
        self.server = ServerAPI()
        self.initUI()

    def initUI(self):
        self.setGeometry(73, 97, 1264, 788)
        self.setStyleSheet(style)

        font = QFont("Helvetica")
        font.setWeight(12)
        font.setPixelSize(20)
        font.setBold(True)
        self.applicationTitle.setFont(font)
        self.applicationTitle.setText("Applications")
        self.applicationTitle.setGeometry(21, 15, 225, 30)

        self.scrollAreaApplications.setGeometry(17, 61, 1230, 727)
        self.scrollAreaApplications.scrollAreaWidgetContents.setGeometry(0, 0, 1230, 727)

        self.addAppButton.setGeometry(1071, 12, 164, 33)
        self.addAppButton.setText("Add new application")
        self.addAppButton.setStyleSheet("background-color: #e3c043;"
                                        "color: black;"
                                        "border-radius: 15px;"
                                        "style: flat;")
        self.addAppButton.setIcon(QIcon('customWidgets/icons/Plus.png'))
        self.addAppButton.setIconSize(QSize(20, 20))
        font.setBold(True)
        font.setWeight(10)
        font.setPixelSize(14)
        self.addAppButton.setFont(font)
        self.addAppButton.clicked.connect(self.addAppButtonClicked)

    def addItem(self, item):
        self.itemList.append(item)
        self.scrollAreaApplications.addItem(item)

    def removeItem(self, item):
        self.itemList.remove(item)
        self.scrollAreaApplications.removeItem(item)

    def clearItems(self):
        self.itemList.clear()
        self.scrollAreaApplications.clearItems()

    def addAppButtonClicked(self):
        self.newAppDialog = NewAppDialog()
        self.newAppDialog.add_app_signal.connect(self.addNewApp)
        self.newAppDialog.show()

    def addNewApp(self, name, version, path):
        self.newAppDialog.hide()
        self.newAppDialog = None
        self.server.addApplication(name, version, path)
