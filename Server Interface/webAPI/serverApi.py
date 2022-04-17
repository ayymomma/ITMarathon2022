import json
import requests


class ServerAPI:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(ServerAPI, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.route = "http://192.168.100.138:3000/api"
        self.token = ""
        self.user = ""

    def login(self, username, password):
        response, code = self.post("/users/login", {"username": username, "password": password})
        if code == 200:
            self.token = json.loads(response)["token"]
            self.user = json.loads(response)["username"]
            return True, json.loads(response)["role"]
        return False, None


    def post(self, endpoint, payload):
        response = requests.post(self.route + endpoint, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
        return response.text, response.status_code

    def getAuthorized(self, endpoint):
        response = requests.get(self.route + endpoint, headers={'Authorization': self.token})
        return response.text, response.status_code

    def postAuthorized(self, endpoint, payload):
        response = requests.post(self.route + endpoint, headers={'Content-Type': 'application/json', 'Authorization': self.token}, data=json.dumps(payload))
        return response.text, response.status_code

    def register(self, username, password):
        response, code = self.post("/users/register", {"username": username, "password": password, "repeatPassword": password})
        if code == 200:
            return True
        return False

    def addDevice(self, deviceId, deviceName):
        response, code = self.postAuthorized("/users/add-device", {"deviceId": deviceId, "deviceName": deviceName})
        print(response, code)
        if code == 201:
            return True
        return False

    def getDevices(self):
        response, code = self.getAuthorized("/users/devices")
        if code == 201:
            return json.loads(response)
        return []

    def addApplication(self, appName, appVersion, appPath):
        response, code = self.postAuthorized("/applications", {"appName": appName})
        if code == 200 or code == 201:
            response, code = self.postAuthorized("/applications/" + appName + "/add_version", {"versionName": appVersion, "appPath": appPath})
            if code == 200 or code == 201:
                return True
        return False

    def getApplications(self):
        response, code = self.getAuthorized("/applications")
        if code == 200 or code == 201:
            return json.loads(response)
        return []

    def getApplicationInfo(self, name):
        response, code = self.getAuthorized("/applications?name=" + name)
        if code == 200 or code == 201:
            return json.loads(response)
        return []

    def addNewVersion(self, appName, appVersion, appPath):
        response, code = self.postAuthorized("/applications/" + appName + "/add_version", {"versionName": appVersion, "appPath": appPath})
        if code == 200 or code == 201:
            return True
        return False

    def getApplicationsForDevice(self, deviceId):
        response, code = self.getAuthorized("/devices/" + deviceId + "/apps")
        if code == 200 or code == 201:
            return json.loads(response)
        return []
