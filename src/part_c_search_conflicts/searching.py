from src.part_a_structures.event_arraylist import EventArrayList


def linear_search_array_partc(event_array, event_id):
    for i in range(event_array.size):
        if event_array.events[i].id == event_id:
            return event_array.events[i]
    return None

def linear_search_linkedlist_partc(event_list, event_id):
    curr = event_list.head
    while curr:
        if curr.event.id == event_id:
            return curr.event
        curr = curr.next
    return None

def binary_search_array_partc(event_array, event_id):
    left, right = 0, event_array.size - 1
    while left <= right:
        mid = (left + right) // 2
        mid_id = event_array.events[mid].id
        if mid_id == event_id:
            return event_array.events[mid]
        elif mid_id < event_id:
            left = mid + 1
        else:
            right = mid - 1
    return None
