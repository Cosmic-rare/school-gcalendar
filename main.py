from lib import joinTime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)
service = build('calendar', 'v3', credentials=creds)

data = joinTime()

for i in data:
    for j in i["subjects"]:
        event = {
            "summary": j["title"],
            "start": {
                "dateTime": j["start"],
                "timeZone": "Japan"
            },
            "end": {
                "dateTime": j["end"],
                "timeZone": "Japan"
            },
            "colorId": j["color"]
        }
        created_event = service.events().insert(calendarId='primary', body=event).execute()
