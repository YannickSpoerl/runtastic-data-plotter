import os, json
from datetime import datetime
from Session import Session


class Parser:

    # TODO: give path manually
    def __init__(self):
        self.sessions = []
        if os.path.exists("User") and os.path.isdir("User"):
            print("'User' directory found and added")
            self.user_dir = "User/"
        else:
            print("'User' directory not found")

        if os.path.exists("Sport-sessions") and os.path.isdir("Sport-sessions"):
            self.sport_sessions_dir = "Sport-sessions/"
            print("'Sport-sessions' directory found and added")
        else:
            print("'Sport-sessions' directory not found")

    def initialize_sport_sessions(self):
        sessions = []
        new_sessions = []
        for file in os.listdir(self.sport_sessions_dir):
            if file[len(file)-5:len(file)] == ".json":
                sessions.append(file)
        for session in sessions:
            with open(self.sport_sessions_dir + session) as data:
                session_data = json.load(data)
            try:
                start_time = datetime.fromtimestamp((session_data["start_time"]+session_data["start_time_timezone_offset"])/1000)
                end_time = datetime.fromtimestamp((session_data["end_time"]+session_data["end_time_timezone_offset"])/1000)
                distance = session_data["distance"]/1000
                duration = round(session_data["duration"]/1000)
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
                id = session_data["id"]
                sport_type_id = session_data["sport_type_id"]
                new_session = Session(start_time, end_time, distance, duration, elevation_gain, elevation_loss,
                                      average_speed, calories, longitude, latitude, max_speed, pause_duration,
                                      pulse_avg, pulse_max, avg_cadence, max_cadence, manual, edited, completed, indoor,
                                      id, sport_type_id)
                new_sessions.append(new_session)
                print("Processed session from " + start_time.strftime("%d.%m.%Y "))
            except:
                print("Couldnt process session " + session)
        self.sessions = new_sessions


p = Parser()
p.initialize_sport_sessions()

