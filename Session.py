class Session:
    def __init__(self, startTime, endTime,
                 distance, duration, elevationGain, elevationLoss, averageSpeed, calories, longitude, latitude, maxSpeed,
                 pauseDuration, pulseAVG, pulseMAX, avgCadence, maxCadence, manual, edited, completed, indoor, id,
                 sportTypeID):
        self.startTime = startTime  # in datetime
        self.endTime = endTime      # in datetime
        self.distance = distance  # in km
        self.duration = duration  # in s
        self.elevationGain = elevationGain  # in m
        self.elevationLoss = elevationLoss  # in m
        self.averageSpeed = averageSpeed  # in km/h
        self.calories = calories
        self.longitude = longitude
        self.latitude = latitude
        self.maxSpeed = maxSpeed  # in km/h
        self.pauseDuration = pauseDuration  # in s
        self.pulseAVG = pulseAVG
        self.pulseMAX = pulseMAX
        self.avgCadence = avgCadence
        self.maxCadence = maxCadence
        self.manual = manual
        self.edited = edited
        self.completed = completed
        self.indoor = indoor
        self.id = id
        self.sportTypeID = sportTypeID
        print("created new session")

    def __str__(self):
        return str(self.distance) + "km, " + str(round(self.duration/60)) + " min from " + self.startTime.strftime("%d.%m.%y")

