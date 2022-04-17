from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

from customWidgets.userFrames.applicationItem import ApplicationItem
from customWidgets.userFrames.scrollAreaApplications import ScrollAreaApplications

style = """
QFrame {
    background-color: #2e2e33;
    border-radius: 10px;
}
"""


class ApplicationsFrame(QFrame):
    def __init__(self, parent):
        super(ApplicationsFrame, self).__init__(parent)
        self.applicationTitle = QLabel(self)
        self.scrollAreaApplications = ScrollAreaApplications(self)
        self.itemList = []
        self.initUI()

    def initUI(self):
        self.setGeometry(411, 97, 926, 788)
        self.setStyleSheet(style)

        font = QFont("Helvetica")
        font.setWeight(12)
        font.setPixelSize(20)
        font.setBold(True)
        self.applicationTitle.setFont(font)
        self.applicationTitle.setText("Applications")
        self.applicationTitle.setGeometry(21, 15, 225, 30)

    def addItem(self, item):
        self.itemList.append(item)
        self.scrollAreaApplications.addItem(item)

    def removeItem(self, item):
        self.itemList.remove(item)
        self.scrollAreaApplications.removeItem(item)

    def clearItems(self):
        self.itemList.clear()
        self.scrollAreaApplications.clearItems()
