from src.part_a_structures.event_linkedlist import Node

from datetime import datetime


def event_key(event):
    return datetime.strptime(f"{event.date} {event.time}", "%Y-%m-%d %H:%M")

#Arr Merge Sort
def merge_sort_array(events):
    if len(events) <= 1:
        return events
    mid = len(events) // 2
    left = merge_sort_array(events[:mid])
    right = merge_sort_array(events[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if event_key(left[i]) <= event_key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



#LL Merge Sort
def merge_sort_linkedlist(head):
    if not head or not head.next:
        return head
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort_linkedlist(head)
    right = merge_sort_linkedlist(next_to_middle)

    return sorted_merge(left, right)

def sorted_merge(a,b):
    if not a:
        return b
    if not b:
        return a

    dummy_node = Node(None)
    tail = dummy_node

    while a and b:
        if event_key(a.event) <= event_key(b.event):
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    if a:
        tail.next = a
    elif b:
        tail.next = b

    return dummy_node.next



def middle(head):
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


