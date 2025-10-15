import random
from datetime import datetime, timedelta

# Event Class
class Event:
    def __init__(self, event_id, title, date, time, location):
        self.id = event_id
        self.title = title
        self.date = date
        self.time = time
        self.location = location

    def __repr__(self):
        return f"Event({self.id}, '{self.title}', {self.date}, {self.time}, '{self.location}')"
