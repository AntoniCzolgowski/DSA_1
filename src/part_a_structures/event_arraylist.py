class EventArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.events = [None] * self.capacity

    def insert(self, event):
        if self.size == self.capacity:
            self._resize()
        self.events[self.size] = event
        self.size += 1

    def _resize(self):
        new_capacity = self.capacity * 2
        new_events = [None] * new_capacity
        for i in range(self.size):
            new_events[i] = self.events[i]
        self.events = new_events
        self.capacity = new_capacity

    def delete(self, event_id):
        for i in range(self.size):
            if self.events[i].id == event_id:
                # shift elements left
                for j in range(i, self.size - 1):
                    self.events[j] = self.events[j + 1]
                self.events[self.size - 1] = None
                self.size -= 1
                return True
        return False

    def search_by_id(self, event_id):
        for i in range(self.size):
            if self.events[i].id == event_id:
                return self.events[i]
        return None

    def list_all(self):
        result = []
        for i in range(self.size):
            result.append(self.events[i])
        return result
