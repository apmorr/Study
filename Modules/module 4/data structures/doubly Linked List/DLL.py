class Node:
    def __init__(self, prev, data, next):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkedBase:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self_size = 0