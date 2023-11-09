class ListQueue:
    def __init__(self):  # creates a queue as a list
        self._L = []

    def enqueue(self, item):  # adds item to end of the list/queue
        self._L.append(item)

    def dequeue(self):  # returns and removes item from the front of the list/queue
        return self._L.pop(0)

    def peek(self):  # returns the first item in the list/queue without removing it
        return self._L[0]

    def __len__(self):  # returns the length of the list/queue
        return len(self._L)

    def is_empty(self):  # returns True if the list/queue is empty
        return len(self._L) == 0

