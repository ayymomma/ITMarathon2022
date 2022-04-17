from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton

style = """
QPushButton {{
    background-color: {bgColor};
    color: {color};
    font-size: 18px;
    border-radius: 12px;
    border: 2px solid;
    border-color: {bdColor};
}}
QPushButton:pressed {{
    background-color: {bgColor};
}}
"""


class CustomButton(QPushButton):

    def __init__(self, parent, text, minimumXSize, maximumXSize, ySize, bgColor="rgba(85, 47, 208, 255)", bdColor="rgba(162, 85, 232, 255)", color="rgba(255, 255, 255, 255)", textWeight=30, bold=True):
        super(CustomButton, self).__init__(parent)
        self.text = text
        self.minXSize = minimumXSize
        self.maxXSize = maximumXSize
        self.ySize = ySize
        self.setStyleSheet(style.format(bgColor=bgColor, bdColor=bdColor, color=color))
        self.setupUi(textWeight, bold)

    def setupUi(self, textWeight, bold):
        font = QFont("Helvetica")
        font.setWeight(textWeight)
        font.setPixelSize(20)
        font.setBold(bold)
        self.setFont(font)
        self.setText(self.text)
        self.setMinimumSize(self.minXSize, self.ySize)
        self.setMaximumSize(self.minXSize, self.ySize)


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
