from src.part_b_sorting.merge_sort import merge_sort_array, merge_sort_linkedlist



#Conflict Detection on Array

def conflict_detection_array(event_array, checked_date):
    sorted_events = merge_sort_array(event_array.list_all())
    same_day_events = []
    for event in sorted_events:
        if event.date == checked_date:
            same_day_events.append(event)

    # Overlapping events
    result = []
    for i in range(len(same_day_events)):
        for j in range(i + 1, len(same_day_events)):
            if same_day_events[i].time == same_day_events[j].time and same_day_events[i].location == same_day_events[j].location:
                result.append((same_day_events[i], same_day_events[j]))
    return result



#Conflict Detection on Linked List

def conflict_detection_linkedlist(event_linkedlist, checked_date):
    event_linkedlist.head = merge_sort_linkedlist(event_linkedlist.head)

    sorted_events = event_linkedlist.to_list()

    same_day_events = []
    for event in sorted_events:
        if event.date == checked_date:
            same_day_events.append(event)

    # Overlapping events
    result = []
    for i in range(len(same_day_events)):
        for j in range(i + 1, len(same_day_events)):
            if same_day_events[i].time == same_day_events[j].time and same_day_events[i].location == same_day_events[j].location:
                result.append((same_day_events[i], same_day_events[j]))

    return result
