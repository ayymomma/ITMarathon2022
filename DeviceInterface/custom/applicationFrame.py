from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

from custom.scrollAreaApplication import ScrollAreaApplications

style = """
QFrame {
    background-color: #2e2e33;
    border-radius: 10px;
    color: white;
}
"""


class ApplicationsFrame(QFrame):
    def __init__(self, parent):
        super(ApplicationsFrame, self).__init__(parent)
        self.newAppDialog = None
        self.applicationTitle = QLabel(self)
        self.scrollAreaApplications = ScrollAreaApplications(self)
        self.itemList = []
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

    def addItem(self, item):
        self.itemList.append(item)
        self.scrollAreaApplications.addItem(item)

    def removeItem(self, item):
        self.itemList.remove(item)
        self.scrollAreaApplications.removeItem(item)

    def clearItems(self):
        self.itemList.clear()
        self.scrollAreaApplications.clearItems()

