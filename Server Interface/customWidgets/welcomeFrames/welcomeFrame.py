from PyQt5.QtWidgets import QFrame

from customWidgets.welcomeFrames.descriptionFrame import DescriptionFrame
from customWidgets.welcomeFrames.loginOrRegisterFrame import LoginOrRegisterFrame


class WelcomeFrame(QFrame):
    def __init__(self, parent):
        super(WelcomeFrame, self).__init__(parent)
        self.descriptionFrame = DescriptionFrame(self)
        self.loginOrRegisterFrame = LoginOrRegisterFrame(self)
        self.initUI()

    def initUI(self):
        self.loginOrRegisterFrame.setGeometry(715, 0, 635, 900)
        self.descriptionFrame.setGeometry(0, 0, 715, 900)
