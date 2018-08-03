class Session:
    def __init__(self, start_time, end_time, distance, duration, elevation_gain, elevation_loss, average_speed,
                 calories, longitude, latitude, max_speed, pause_duration, pulse_avg, pulse_max, avg_cadence,
                 max_cadence, manual, edited, completed, indoor, session_id, sport_type_id):
        self.date = start_time.strftime("%d.%m.")
        self.start_time = start_time  # in datetime
        self.end_time = end_time      # in datetime
        self.distance = distance  # in km
        self.duration = duration  # in s
        self.elevation_gain = elevation_gain  # in m
        self.elevation_loss = elevation_loss  # in m
        self.average_speed = average_speed  # in km/h
        self.calories = calories
        self.longitude = longitude
        self.latitude = latitude
        self.max_speed = max_speed  # in km/h
        self.pause_duration = pause_duration  # in s
        self.pulse_avg = pulse_avg
        self.pulse_max = pulse_max
        self.avg_cadence = avg_cadence
        self.max_cadence = max_cadence
        self.manual = manual
        self.edited = edited
        self.completed = completed
        self.indoor = indoor
        self.session_id = session_id
        self.sport_type_id = sport_type_id
        self.data = dict([("start_time", start_time.strftime("%d.%m.")), ("end_time", end_time.strftime("%d.%m.")),
                          ("distance", distance),
                          ("duration", duration), ("elevation_gain", elevation_gain),
                          ("elevation_loss", elevation_loss), ("average_speed", average_speed), ("calories", calories),
                          ("longitude", longitude), ("latitude", latitude), ("max_speed", max_speed),
                          ("pause_duration", pause_duration), ("pulse_avg", pulse_avg), ("pulse_max", pulse_max),
                          ("avg_cadence", avg_cadence), ("max_cadence", max_cadence), ("manual", manual),
                          ("edited", edited), ("completed", completed), ("indoor", indoor), ("session_id", session_id),
                          ("sport_type_id", sport_type_id), ("date", self.date)])

    def __str__(self):
        return str(self.distance) + "km, " + str(round(self.duration/60)) + " min from " + \
               self.start_time.strftime("%d.%m.%y")

    def __lt__(self, other):
        return self.start_time < other.start_time

    def __gt__(self, other):
        return self.start_time > other.start_time

