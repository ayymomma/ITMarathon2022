import json
import threading
import time

import requests

from deviceDataReader import DeviceDataReader


class ServerAPI:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(ServerAPI, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.route = "http://192.168.100.138:3000/api"
        self.device_id = ""
        self.device_name = ""

        self.device_data_reader = DeviceDataReader()

    def connect(self, device_id):
        response, code = self.post("/devices/connect", {"deviceId": device_id})
        print(response)
        if code == 200:
            self.device_id = json.loads(response)["deviceId"]
            self.device_name = json.loads(response)["deviceName"]
            threading.Thread(target=self.keep_alive).start()

            self.send_apps_versions()

            return True

        return False

    def keep_alive(self):
        while True:
            self.post("/devices/keepAlive", {"deviceId": self.device_id})
            time.sleep(50)

    def post(self, endpoint, payload):
        response = requests.post(self.route + endpoint, headers={'Content-Type': 'application/json'},
                                 data=json.dumps(payload))
        return response.text, response.status_code

    def postAuthorized(self, endpoint, payload):
        response = requests.post(self.route + endpoint,
                                 headers={'Content-Type': 'application/json', 'Authorization': self.token},
                                 data=json.dumps(payload))
        return response.text, response.status_code

    @classmethod
    def get_device_name(cls):
        return cls.__instance.device_name

    def send_apps_versions(self):
        # appName
        # versionName
        apps = self.device_data_reader.get_app_list()
        print(apps)
        self.post(f"/devices/{self.device_id}/save-apps", apps)


