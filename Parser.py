import os


class Session:
    def __init__(self, startTime, endTime, createdAt, updatedAt, startTimeTimezoneOffset, endTimeTimezoneOffset,
                 distance, duration, elevationGain, elevationLoss, averageSpeed, calories, longitude, latitude,
                 maxSpeed, pauseDuration, durationPerKM, pulseAVG, pulseMAX, avgCadence, maxCadence, manual, edited,
                 completed, liveTrackingActive, liveTrackingEnabled, cheeringEnabled, indoor, id, sportTypeID):
        self.startTime = startTime
        self.endTime = endTime
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.startTimeTimezoneOffset = startTimeTimezoneOffset
        self.endTimeTimezoneOffset = endTimeTimezoneOffset
        self.distance = distance
        self.duration = duration
        self.elevationGain = elevationGain
        self.elevationLoss = elevationLoss
        self.averageSpeed = averageSpeed
        self.calories = calories
        self.longitude = longitude
        self.latitude = latitude
        self.maxSpeed = maxSpeed
        self.pauseDuration = pauseDuration
        self.durationPerKM = durationPerKM
        self.pulseAVG = pulseAVG
        self.pulseMAX = pulseMAX
        self.avgCadence = avgCadence
        self.maxCadence = maxCadence
        self.manual = manual
        self.edited = edited
        self.completed = completed
        self.liveTrackingActive = liveTrackingActive
        self.liveTrackingEnabled = liveTrackingEnabled
        self.cheeringEnabled = cheeringEnabled
        self.indoor = indoor
        self.id = id
        self.sportTypeID = sportTypeID


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
        for session in files:
            if session[len(session)-5:len(session)] == ".json":
                sessions.append(session)
        if sessions:
            print("Warning: Your have 0 sessions!")
        self.sport_sessions = sessions
        return sessions


p = Parser()
sportSessions = p.initialize_sport_sessions()
