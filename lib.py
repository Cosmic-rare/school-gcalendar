import json

def loadSetting():
    with open("setting.json") as fSetting:
        return json.load(fSetting)
