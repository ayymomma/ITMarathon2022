from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QFrame, QLabel, QPushButton

from customWidgets.buttons.customButton import CustomButton
from customWidgets.userFrames.applicationsFrame import ApplicationsFrame
from customWidgets.userFrames.deviceItem import DeviceItem
from customWidgets.userFrames.devicesFrame import DevicesFrame
from customWidgets.userFrames.newDeviceDialog import NewDeviceDialog
from webAPI.serverApi import ServerAPI

style = """
QFrame {
    background-color: #171719;
}
QLabel {
    color: #FFFFFF;
}
"""


class UserFrame(QFrame):
    def __init__(self, parent):
        super(UserFrame, self).__init__(parent)
        self.newDeviceDialog = None
        self.welcomeLabel = QLabel(self)
        self.devicesFrame = DevicesFrame(self)
        self.applicationsFrame = ApplicationsFrame(self)
        self.addDeviceButton = CustomButton(self, "", 218, 238, 43)
        self.server = ServerAPI()
        self.initUI()

    def initUI(self):
        self.setStyleSheet(style)
        self.setGeometry(0, 0, 1350, 900)

        font = QFont("Helvetica")
        font.setWeight(20)
        font.setPixelSize(30)
        font.setBold(True)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setGeometry(90, 25, 300, 30)
        self.welcomeLabel.setText("Welcome!")

        self.addDeviceButton.setGeometry(116, 825, 218, 43)
        self.addDeviceButton.setText("Add new device")
        self.addDeviceButton.setStyleSheet("background-color: #5AE343;"
                                           "color: black;"
                                           "border-radius: 20px;"
                                           "style: flat;")
        self.addDeviceButton.setIcon(QIcon('customWidgets/icons/Plus.png'))
        self.addDeviceButton.setIconSize(QSize(30, 30))
        font.setBold(False)
        font.setWeight(10)
        font.setPixelSize(20)
        self.addDeviceButton.setFont(font)
        self.addDeviceButton.clicked.connect(self.addDeviceButtonClicked)
        
    def addDeviceButtonClicked(self):
        self.newDeviceDialog = NewDeviceDialog(self)
        self.newDeviceDialog.add_signal.connect(self.addNewDevice)
        self.newDeviceDialog.show()

    def addNewDevice(self, name, id):
        self.newDeviceDialog.hide()
        self.newDeviceDialog = None
        device = DeviceItem()
        device.setName(name)
        device.setDeviceId(id)
        if self.server.addDevice(id, name):
            self.devicesFrame.addDevice(device)

    def show(self):
        super(UserFrame, self).show()
        deviceList = self.server.getDevices()
        for device in deviceList:
            print(device)
            dev = DeviceItem()
            # dev.add_apps_signal.connect(self.addApps)
            dev.setName(device['deviceName'])
            dev.setDeviceId(device['deviceId'])
            self.devicesFrame.addDevice(dev)

    # def addApps(self, apps):
    #     for app in apps:
    #         self.applicationsFrame.addItem(app)





