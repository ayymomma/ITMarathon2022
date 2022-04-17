from PyQt5.QtWidgets import QFrame


class DescriptionFrame(QFrame):
    def __init__(self, parent):
        super(DescriptionFrame, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: rgba(85, 47, 208, 255);")
