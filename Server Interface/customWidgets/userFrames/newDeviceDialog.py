from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QDialog, QLineEdit, QTextEdit

from customWidgets.buttons.customButton import CustomButton

style = """
QDialog {
    background-color: #171719;
}
QLineEdit {
    background-color: #45454c;
}
"""


class NewDeviceDialog(QDialog):
    add_signal = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(NewDeviceDialog, self).__init__(parent)

        self.deviceName = QLineEdit(self)
        self.deviceId = QLineEdit(self)
        self.addButton = CustomButton(self, "Add", 158, 178, 43, bgColor="#5AE343", bdColor="#5AE343", color="#000000", textWeight=10, bold=False)
        self.setWindowTitle("New Device")
        self.initUI()

    def initUI(self):
        self.setFixedSize(683, 456)
        self.setStyleSheet(style)
        self.deviceName.setPlaceholderText("Device name")
        self.deviceName.setGeometry(58, 68, 568, 48)
        self.deviceName.setFont(QFont("Arial", 15))
        self.deviceName.setAlignment(Qt.AlignCenter)
        self.deviceName.setStyleSheet("border: None; border-radius: 10px;")

        self.deviceId.setPlaceholderText("Device id")
        self.deviceId.setGeometry(58, 147, 568, 48)
        self.deviceId.setFont(QFont("Arial", 15))
        self.deviceId.setAlignment(Qt.AlignCenter)
        self.deviceId.setStyleSheet("border: None; border-radius: 10px;")

        self.addButton.setGeometry(263, 383, 158, 43)
        self.addButton.setIcon(QIcon('customWidgets/icons/Plus.png'))
        self.addButton.clicked.connect(self.addButtonClick)

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

    def addButtonClick(self):
        self.add_signal.emit(self.deviceName.text(), self.deviceId.text())
