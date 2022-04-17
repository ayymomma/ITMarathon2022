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


class LoginButton(QPushButton):

    def __init__(self, parent):
        super(LoginButton, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        font = QFont("Helvetica")
        font.setWeight(30)
        font.setPixelSize(20)
        font.setBold(True)
        self.setFont(font)
        self.setText("LOG IN")
        self.setMinimumSize(115, 35)
        self.setMaximumSize(115, 35)
        self.setStyleSheet(style)

    def enterEvent(self, event: QtCore.QEvent):
        super(LoginButton, self).enterEvent(event)
        self.setMinimumSize(135, 35)
        self.setMaximumSize(135, 35)
        self.setGeometry(self.pos().x() - 10, self.pos().y(), self.width() + 10, self.height())

    def leaveEvent(self, event: QtCore.QEvent):
        super(LoginButton, self).leaveEvent(event)
        self.setMinimumSize(115, 35)
        self.setMaximumSize(115, 35)
        self.setGeometry(self.pos().x() + 10, self.pos().y(), self.width() - 10, self.height())