#Formal tests

def test_array_no_conflicts():
    arr = EventArrayList()
    e1 = Event(1, "Exam", "2025-07-10", "10:00", "Room 101")
    e2 = Event(2, "Workshop", "2025-07-10", "11:00", "Room 101")
    e3 = Event(3, "Concert", "2025-07-10", "10:00", "Main Hall")
    for e in [e1, e2, e3]:
        arr.insert(e)
    checked_date = "2025-07-10"
    result = conflict_detection_array(arr, checked_date)
    print("PASSED" if result == [] else "FAILED")


def test_array_with_conflicts():
    arr = EventArrayList()
    e1 = Event(1, "Exam", "2025-09-10", "10:00", "Main Hall")
    e2 = Event(2, "Workshop", "2025-09-10", "10:00", "Main Hall")
    e3 = Event(3, "Concert", "2025-09-10", "10:00", "Main Hall")
    for e in [e1, e2, e3]:
        arr.insert(e)
    checked_date = "2025-09-10"
    result = conflict_detection_array(arr, checked_date)
    print("PASSED" if len(result) > 0 else "FAILED")


def test_linkedlist_no_conflicts():
    ll = EventLinkedList()
    e1 = Event(1, "Exam", "2025-07-10", "10:00", "Room 101")
    e2 = Event(2, "Workshop", "2025-07-10", "11:00", "Room 101")
    e3 = Event(3, "Concert", "2025-07-10", "10:00", "Main Hall")
    for e in [e1, e2, e3]:
        ll.append(e)
    checked_date = "2025-07-10"
    result = conflict_detection_linkedlist(ll, checked_date)
    print("PASSED" if result == [] else "FAILED")


def test_linkedlist_with_conflicts():
    ll = EventLinkedList()
    e1 = Event(1, "Exam", "2025-09-10", "10:00", "Main Hall")
    e2 = Event(2, "Workshop", "2025-09-10", "10:00", "Main Hall")
    e3 = Event(3, "Concert", "2025-09-10", "10:00", "Main Hall")
    for e in [e1, e2, e3]:
        ll.append(e)
    checked_date = "2025-09-10"
    result = conflict_detection_linkedlist(ll, checked_date)
    print("PASSED" if len(result) > 0 else "FAILED")

