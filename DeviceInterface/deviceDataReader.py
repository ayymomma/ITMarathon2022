import json


class DeviceDataReader:
    def __init__(self):
        self.data = []

    def read(self):
        with open('device_data.json') as f:
            # returns JSON object as
            # a dictionary
            self.data = json.load(f)
        return self.data
