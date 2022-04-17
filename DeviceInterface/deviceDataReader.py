import json
import os
from os import walk


class DeviceDataReader:
    # singleton
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(DeviceDataReader, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.data = []
        self.apps = []
        self.read()
        self.read_apps()

    def read(self):
        with open('device_data.json') as f:
            # returns JSON object as
            # a dictionary
            self.data = json.load(f)
        return self.data

    def read_apps(self):
        for app in next(walk(os.getcwd() + "\\apps"), (None, None, []))[2]:
            with open(os.getcwd() + "\\apps\\" + app) as f:
                self.apps.append(json.load(f))

        return self.apps

    @classmethod
    def get_applications(cls):
        return cls.__instance.apps

    def get_app_list(self):
        appList = []
        for app in self.apps:
            appList.append({"appName": app["app_name"], "versionName": app["version_id"]})
        return appList
