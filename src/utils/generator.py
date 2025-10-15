from datetime import datetime, timedelta
import random
from src.part_a_structures.event import Event

# Random Event Generator

def generate_random_events(n):
    titles = ["Hackathon", "Concert", "Seminar", "Exam", "Workshop", "Meetup"]
    locations = ["Auditorium", "Main Hall", "Room 101", "Lab A", "Cafeteria", "Library"]
    base_date = datetime(2025, 1, 1)

    events = []
    for i in range(n):
        title = random.choice(titles)
        date = (base_date + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
        time = f"{random.randint(8, 20):02d}:{random.choice(['00','30'])}"
        location = random.choice(locations)
        events.append(Event(i, title, date, time, location))
    return events
