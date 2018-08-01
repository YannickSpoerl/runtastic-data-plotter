import os, json
from datetime import datetime
from Session import Session


class Parser:
    def __init__(self):
        self.sport_sessions = []
        if os.path.exists("User") and os.path.isdir("User"):
            print("'User' directory found and added")
            self.userDirexists = True
        else:
            print("'User' directory not found")

        if os.path.exists("Sport-sessions") and os.path.isdir("Sport-sessions"):
            print("'Sport-sessions' directory found and added")
        else:
            print("'Sport-sessions' directory not found")
            print("Please make sure the script lays in the same directory as the 'Sport-sessions directory, otherwise "
                  "no data can be retrieved!")

    def initialize_sport_sessions(self):
        files = os.listdir("Sport-sessions")
        sessions = []
        for file in files:
            if file[len(file)-5:len(file)] != ".json":
                files.remove(file)
        for file in files:
            with open("Sport-sessions/" + file) as data:
                sessions.append(json.load(data))
        dates = []
        for session in sessions:
            dates.append(datetime.fromtimestamp(session["start_time"]/1000+7200))
        dates.sort()
        for date in dates:
            print(date)


p = Parser()
p.initialize_sport_sessions()

