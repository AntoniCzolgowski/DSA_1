import random
from datetime import datetime, timedelta
import time


# Event Class
class Event:
    def __init__(self, event_id, title, date, time, location):
        self.id = event_id
        self.title = title
        self.date = date
        self.time = time
        self.location = location
        self.timestamp = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

    def __repr__(self):
        return (f"Event({self.id}, '{self.title}', '{self.date}', '{self.time}', "
                f"'{self.location}', timestamp='{self.timestamp.strftime('%Y-%m-%d %H:%M')}')")