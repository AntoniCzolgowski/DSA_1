from src.part_a_structures.event import Event
from src.part_a_structures.event_arraylist import EventArrayList
from src.part_a_structures.event_linkedlist import EventLinkedList
from src.utils.generator import generate_random_events



# Pytest Tests
def test_array_insert_and_search():
    store = EventArrayList()
    e = Event(1, "Hackathon", "2025-10-10", "10:00", "Auditorium")
    store.insert(e)
    assert store.search_by_id(1) == e

def test_array_delete():
    store = EventArrayList()
    e = Event(2, "Concert", "2025-11-01", "19:00", "Main Hall")
    store.insert(e)
    assert store.delete(2) is True
    assert store.search_by_id(2) is None

def test_linked_insert_and_search():
    store = EventLinkedList()
    e = Event(3, "Exam", "2025-12-01", "09:00", "Room 101")
    store.insert(e)
    assert store.search_by_id(3) == e

def test_linked_delete():
    store = EventLinkedList()
    e = Event(4, "Workshop", "2025-09-15", "14:00", "Lab A")
    store.insert(e)
    assert store.delete(4) is True
    assert store.search_by_id(4) is None

def test_bulk_generation():
    events = generate_random_events(500)
    assert len(events) == 500
    assert all(isinstance(e, Event) for e in events)
