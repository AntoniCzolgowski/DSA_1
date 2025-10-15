def event_key(event):
    return datetime.strptime(f"{event.date} {event.time}", "%Y-%m-%d %H:%M")


#Quick sort on Dynamic Array
def quick_sort_array(events):
    if len(events) <= 1:
        return events
    pivot = events[len(events) // 2]
    left = [x for x in events if event_key(x) < event_key(pivot)]
    middle = [x for x in events if event_key(x) == event_key(pivot)]
    right = [x for x in events if event_key(x) > event_key(pivot)]
    return quick_sort_array(left) + middle + quick_sort_array(right)




#Quick Sort Linked List
def quick_sort_linkedlist(ll):
    events = ll.to_list()
    events = quick_sort_array(events)
    ll.from_list(events)
