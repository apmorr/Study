from Linked_List import LinkedList      # imports the LinkedList class from the Linked_List file

class LinkedQueue:
    def __init__(self):
        self._L = LinkedList()                      # creates the list/queue as a data structures

    def enqueue(self, item):
        self._L.addlast(item)                       # calls the addlast() function because queues add items to the back

    def dequeue(self):
        return self._L.removefirst()                # calls the removefirst() function because queues remove items in the front


    def peek(self):
        item = self._L.removefirst()                # creates a value to store the data of the first node in the queue but also removes it from the front of queue
        self._L.addfirst(item)                      # adds node that was just removed to the front of the list
        return item                                 # returns the item from the first node



    def __len__(self):
        return len(self._L)

    def is_empty(self):
        return len(self) == 0