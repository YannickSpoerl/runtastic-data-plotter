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
        print("created new session")

