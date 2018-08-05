import json
import os
from datetime import datetime
from Session import Session


class Parser:

    def __init__(self, path=os.getcwd()):
        rel_path = os.path.relpath(path, os.getcwd()) + "/Sport-sessions"
        self.sessions = []
        self.sport_sessions_dir_validated = False
        if os.path.exists(rel_path) and os.path.isdir(rel_path):
            self.sport_sessions_dir = rel_path
            print("'Sport-sessions' directory found at " + rel_path)
            self.sport_sessions_dir_validated = True
        else:
            print("'Sport-sessions' directory not found. Possible Errors: \n -the directory where the sessions lie is"
                  "not named 'Sport-sessions': Fix it by renaming it correctly. \n -you gave the wrong path. "
                  "Fix it by giving the correct path. \n -General fix: just put the 'Sport-sessions directory in the "
                  "same directory as this script.")

    def initialize_sport_sessions(self):
        if not self.sport_sessions_dir_validated:
            print("Can't initialize sessions without giving a valid directory!")
            return
        sessions = []
        new_sessions = []
        for file in os.listdir(self.sport_sessions_dir):
            if file[len(file)-5:len(file)] == ".json":
                sessions.append(file)
        print("Initializing sessions...")
        number_of_sessions = 0
        for session in sessions:
            with open(self.sport_sessions_dir + "/" + session) as data:
                session_data = json.load(data)
            try:
                start_time = datetime.fromtimestamp((session_data["start_time"] +
                                                     session_data["start_time_timezone_offset"])/1000)
                end_time = datetime.fromtimestamp((session_data["end_time"] +
                                                   session_data["end_time_timezone_offset"])/1000)
                distance = session_data["distance"]/1000
                duration = session_data["duration"]/60000
                elevation_gain = session_data["elevation_gain"]
                elevation_loss = session_data["elevation_loss"]
                average_speed = session_data["average_speed"]
                calories = session_data["calories"]
                longitude = session_data["longitude"]
                latitude = session_data["latitude"]
                max_speed = session_data["max_speed"]
                pause_duration = round(session_data["pause_duration"]/1000)
                pulse_avg = session_data["pulse_avg"]
                pulse_max = session_data["pulse_max"]
                avg_cadence = session_data["avg_cadence"]
                max_cadence = session_data["max_cadence"]
                manual = session_data["manual"]
                edited = session_data["edited"]
                completed = session_data["completed"]
                indoor = session_data["indoor"]
                session_id = session_data["id"]
                sport_type_id = session_data["sport_type_id"]
                new_session = Session(start_time, end_time, distance, duration, elevation_gain, elevation_loss,
                                      average_speed, calories, longitude, latitude, max_speed, pause_duration/60,
                                      pulse_avg, pulse_max, avg_cadence, max_cadence, manual, edited, completed, indoor,
                                      session_id, sport_type_id)
                new_sessions.append(new_session)
                number_of_sessions += 1
            except:
                print("Couldnt process session " + session)
        new_sessions.sort()
        print(str(number_of_sessions) + " Sessions initialized")
        self.sessions = new_sessions
