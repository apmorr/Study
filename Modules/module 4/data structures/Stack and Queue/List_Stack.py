class ListStack:
    def __init__(self):
        self._L = []                #creating a Stack/List inside a class

    def __len__(self):
        return len(self._L)            #returns the number of elements in the Stack/List

    def is__empty(self):
        return len(self._L) == 0       #returns if the List/Stack is empty or not

    def push(self, e):
        self._L.append(e)               #adds an element to the end of a List/Stack

    def pop(self):
        return self._L.pop()            #removes the lat element in the List/Stack and returns it

    def peek(self):
        return self._L[-1]              #returns the last element is the List/Stack without removing it