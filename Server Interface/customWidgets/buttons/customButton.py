from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton

style = """
QPushButton {
    background-color: rgba(85, 47, 208, 255);
    color: #FFFFFF;
    font-size: 18px;
    border-radius: 15px;
    border: 2px solid;
    border-color: rgba(162, 85, 232, 255);
}
QPushButton:pressed {
    background-color: rgba(85, 47, 208, 255);
}
"""


class CustomButton(QPushButton):

    def __init__(self, parent, text, minimumXSize, maximumXSize, ySize):
        super(CustomButton, self).__init__(parent)
        self.text = text
        self.minXSize = minimumXSize
        self.maxXSize = maximumXSize
        self.ySize = ySize
        self.setupUi()

    def setupUi(self):
        font = QFont("Helvetica")
        font.setWeight(30)
        font.setPixelSize(20)
        font.setBold(True)
        self.setFont(font)
        self.setText(self.text)
        self.setMinimumSize(self.minXSize, self.ySize)
        self.setMaximumSize(self.minXSize, self.ySize)
        self.setStyleSheet(style)

    def enterEvent(self, event: QtCore.QEvent):
        super(CustomButton, self).enterEvent(event)
        self.setMinimumSize(self.maxXSize, self.ySize)
        self.setMaximumSize(self.maxXSize, self.ySize)
        self.setGeometry(self.pos().x() - 10, self.pos().y(), self.width() + 10, self.height())

    def leaveEvent(self, event: QtCore.QEvent):
        super(CustomButton, self).leaveEvent(event)
        self.setMinimumSize(self.minXSize, self.ySize)
        self.setMaximumSize(self.minXSize, self.ySize)
        self.setGeometry(self.pos().x() + 10, self.pos().y(), self.width() - 10, self.height())
