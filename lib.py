import json

def loadSetting():
    with open("setting.json") as fSetting:
        return json.load(fSetting)

def loadData():
    with open("data.json") as fData:
        return json.load(fData)
