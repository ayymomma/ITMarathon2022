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


class NewVersionDialog(QDialog):
    add_vers_signal = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(NewVersionDialog, self).__init__(parent)

        self.appVersion = QLineEdit(self)
        self.appPath = QLineEdit(self)
        self.uploadButton = CustomButton(self, "upload", 158, 178, 43, bgColor="#5AE343", bdColor="#5AE343", color="#000000", textWeight=10, bold=False)
        self.setWindowTitle("New Application")
        self.initUI()

    def initUI(self):
        self.setFixedSize(683, 456)
        self.setStyleSheet(style)

        self.appVersion.setPlaceholderText("Application version")
        self.appVersion.setGeometry(58, 228, 568, 48)
        self.appVersion.setFont(QFont("Arial", 15))
        self.appVersion.setAlignment(Qt.AlignCenter)
        self.appVersion.setStyleSheet("border: None; border-radius: 10px;")

        self.appPath.setPlaceholderText("Application path")
        self.appPath.setGeometry(58, 309, 568, 48)
        self.appPath.setFont(QFont("Arial", 15))
        self.appPath.setAlignment(Qt.AlignCenter)
        self.appPath.setStyleSheet("border: None; border-radius: 10px;")

        self.uploadButton.setGeometry(263, 383, 158, 43)
        self.uploadButton.setIcon(QIcon('customWidgets/icons/Upload.png'))
        self.uploadButton.clicked.connect(self.addAppButtonClick)

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

    def addAppButtonClick(self):
        self.add_vers_signal.emit(self.appVersion.text(), self.appPath.text())
