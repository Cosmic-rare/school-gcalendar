import json
from datetime import date, datetime, timedelta

def loadSetting():
    with open("setting.json") as fSetting:
        return json.load(fSetting)

def loadData():
    with open("data.json") as fData:
        return json.load(fData)

def getFirstDay():
    d = datetime.strptime(loadData()["start"], '%y/%m/%d')
    return date(d.year, d.month, d.day)

def joinSubject():
    d = getFirstDay()
    subjectSetting = loadSetting()["subjects"]
    joinedSubject = []
    for i in loadData()["subjects"]:
        joined = []
        for j in i:
            joined.append(subjectSetting[j])
        joinedSubject.append({ "date": d, "subjects": joined })
        d = d + timedelta(days=1)
    return joinedSubject

def joinTime():
    joinedSubject = joinSubject()
    schedule = loadSetting()["schedules"][loadData()["schedule"]]
    for i in range(len(joinedSubject)):
        for j in range(len(joinedSubject[i]["subjects"])):
            joinedSubject[i]["subjects"][j]["start"] = "{}T{}:00".format(joinedSubject[i]["date"].isoformat(), schedule[j][0])
            joinedSubject[i]["subjects"][j]["end"] = "{}T{}:00".format(joinedSubject[i]["date"].isoformat(), schedule[j][1])
    return joinedSubject

