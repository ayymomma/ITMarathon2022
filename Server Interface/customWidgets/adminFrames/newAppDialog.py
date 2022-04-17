from PyQt5.QtCore import Qt
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


class NewAppDialog(QDialog):
    def __init__(self, parent=None):
        super(NewAppDialog, self).__init__(parent)

        self.appName = QLineEdit(self)
        self.appVersion = QLineEdit(self)
        self.appPath = QLineEdit(self)
        self.uploadButton = CustomButton(self, "upload", 158, 178, 43, bgColor="#5AE343", bdColor="#5AE343", color="#000000", textWeight=10, bold=False)
        self.setWindowTitle("New Application")
        self.initUI()

    def initUI(self):
        self.setFixedSize(683, 456)
        self.setStyleSheet(style)
        self.appName.setPlaceholderText("Application name")
        self.appName.setGeometry(58, 68, 568, 48)
        self.appName.setFont(QFont("Arial", 15))
        self.appName.setAlignment(Qt.AlignCenter)
        self.appName.setStyleSheet("border: None; border-radius: 10px;")

        self.appVersion.setPlaceholderText("Application version")
        self.appVersion.setGeometry(58, 147, 568, 48)
        self.appVersion.setFont(QFont("Arial", 15))
        self.appVersion.setAlignment(Qt.AlignCenter)
        self.appVersion.setStyleSheet("border: None; border-radius: 10px;")

        self.appPath.setPlaceholderText("Application path")
        self.appPath.setGeometry(58, 228, 568, 48)
        self.appPath.setFont(QFont("Arial", 15))
        self.appPath.setAlignment(Qt.AlignCenter)
        self.appPath.setStyleSheet("border: None; border-radius: 10px;")

        self.uploadButton.setGeometry(263, 383, 158, 43)
        self.uploadButton.setIcon(QIcon('customWidgets/icons/Upload.png'))

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

