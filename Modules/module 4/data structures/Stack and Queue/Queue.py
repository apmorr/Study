class Queue:
    def __init__(self):
        self.head = 0                       #this is the pointer variable that stores the index of the first item in the queue
        self._L = []

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        item = self._L[self.head]           #creates a local 'item' variable to store the current element at the head pointer
        self.head += 1                      #assigns the next element as the head pointer, making that element the new start of the queue
        return item                             #we dont have to actaully delete the old head of the queue, instead we can leave it in the list and change it to a new element when we need to
                                                #this works because our queue is not the list, but it is all the elements in the list between our pointers
                                                #a list is not a queue, but a queue can be a list

    def peek(self):
        return self._L[self.head]           #instead of returning the element at the index of 0, we can return the element at the index of the head pointer
                                            #the index of 0 in our list is the start of our list and may not always be the start of our queue
                                            #so by using the head pointer we can always return the element at the start of our queue

    def __len__(self):
        return len(self._L) - self.head     #finds the length of the list, and subtracts the index of the head pointer
                                            #this works because if the start of our queue is in the middle of the list we dont want the length of the entire list returned

    def is_empty(self):
        return len(self._L) == 0
    