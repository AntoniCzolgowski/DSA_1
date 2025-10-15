from datetime import datetime

def event_key(event):
    return datetime.strptime(f"{event.date} {event.time}", "%Y-%m-%d %H:%M")

#Insertion sort on Dynamic Array
def insertion_sort_array(event_list):
    for i in range(1, event_list.size):
        key_event = event_list.events[i]
        key_value = key_event.timestamp
        j = i - 1
        while j >= 0 and event_list.events[j].timestamp > key_value:
            event_list.events[j + 1] = event_list.events[j]
            j -= 1
        event_list.events[j + 1] = key_event

#Insertion sort on Linked List
def insertion_sort_linkedlist(ll):
    sorted_head = None
    current = ll.head
    while current:
        next_node = current.next
        sorted_head = sorted_insert_fast(sorted_head, current)
        current = next_node
    ll.head = sorted_head


def sorted_insert_fast(head, new_node):
    if not head or new_node.event.timestamp < head.event.timestamp:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.event.timestamp < new_node.event.timestamp:
        current = current.next

    new_node.next = current.next
    current.next = new_node
    return head

