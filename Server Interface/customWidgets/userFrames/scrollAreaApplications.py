from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea, QSpacerItem, QSizePolicy, QWidget, QVBoxLayout, QFrame, QLayout


class ScrollAreaApplications(QScrollArea):
    def __init__(self, parent=None):
        super(ScrollAreaApplications, self).__init__(parent=parent)

        self.scrollAreaWidgetContents = QWidget()
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.setup_ui()

    def setup_ui(self):
        self.setGeometry(10, 61, 907, 727)
        self.setStyleSheet("background-color: #2e2e33;")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(907, 727)
        self.setFrameShape(QFrame.NoFrame)
        self.setLineWidth(0)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setAlignment(Qt.AlignCenter)

        self.scrollAreaWidgetContents.setGeometry(0, 0, 907, 727)

        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout.setSpacing(10)

        self.verticalLayout.addSpacerItem(self.spacerItem)

        self.setWidget(self.scrollAreaWidgetContents)

    def addWidget(self, widget):
        self.verticalLayout.removeItem(self.spacerItem)
        self.verticalLayout.addWidget(widget)
        self.verticalLayout.addItem(self.spacerItem)

