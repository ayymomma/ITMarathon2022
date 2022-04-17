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
        print(response)
        if code == 200:
            self.token = json.loads(response)["token"]
            self.user = json.loads(response)["username"]
            return True, json.loads(response)["role"]
        return False, None


    def post(self, endpoint, payload):
        response = requests.post(self.route + endpoint, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
        return response.text, response.status_code

    def postAuthorized(self, endpoint, payload):
        response = requests.post(self.route + endpoint, headers={'Content-Type': 'application/json', 'Authorization': self.token}, data=json.dumps(payload))
        return response.text, response.status_code

    def register(self, username, password):
        response, code = self.post("/users/register", {"username": username, "password": password, "repeatPassword": password})
        print(response, code)
        if code == 200:
            return True
        return False

    def addDevice(self, deviceId, deviceName):
        response, code = self.postAuthorized("/users/add-device", {"deviceId": deviceId, "deviceName": deviceName})
        print(response, code)
        if code == 201:
            return True
        return False
