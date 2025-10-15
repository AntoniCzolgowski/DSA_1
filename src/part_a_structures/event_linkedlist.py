class Node:
    def __init__(self, event):
        self.event = event
        self.next = None

class EventLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, event):
        new_node = Node(event)
        new_node.next = self.head
        self.head = new_node

    def delete(self, event_id):
        current = self.head
        prev = None
        while current:
            if current.event.id == event_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def search_by_id(self, event_id):
        current = self.head
        while current:
            if current.event.id == event_id:
                return current.event
            current = current.next
        return None

    def list_all(self):
        result = []
        current = self.head
        while current:
            result.append(current.event)
            current = current.next
        return result
