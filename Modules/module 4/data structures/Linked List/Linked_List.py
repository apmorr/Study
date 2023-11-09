class Node:
    def __init__(self, data, next=None):
        self.data = data                # the data stored in the node
        self.next = next                # the address of the next node, acts as a pointer to the next node



class LinkedList:
    def __init__(self):
        self.head = None                        # the head node is 'None' by default because our list is empty
        self.tail = None

    def addfirst(self, item):  # O(1)
        self.head = Node(item, self.head)
        if self.tail is None: self.tail = self.head         # creates a new node passing in the element as the node data, and the current head node address as the next nodes address
                                                            # then adds the new node to the front of the list and assigns the new node as the head node
                                                            #if the tail node is 'None' then set the tail node to the head node


    def removefirst(self):  # O(1)
        item = self.head.data                               # creates an item variable to store the data of the head node
        self.head = self.head.next                          # assigns the head node to the node next to it
        if self.head is None: self.tail = None              # returns the data of the previous head node
        return item                                             # like the queue we dont have to delete the node from our linked list
                                                                # instead we can just reassign the values of the node when we need to


    def addlast(self, item):  # O(1)
        if self.head is None:                                   # check to see if head is empty
            self.addfirst(item)                                 # if head is None, calls addfirst() instead
        else:
            self.tail.next = Node(item)                         # if head isnt empty, set the current tail node pointer to the new node so its not 'None'
            self.tail = self.tail.next                          # then set the tail node to the new node



    def removelast(self):  # O(n), has to iterate through the List
        if self.head is self.tail:                              # if head and tail are the same that means theres only one node,
            return self.removefirst()                           # because theres only one node we can save time by calling the remove first method
        else:
            curr = self.head                                    # creates a value to store the current head node
            while curr.next is not self.tail:                   # checks that the current pointer is not the tail node
                curr = curr.link                                # sets the current node to the next node, traversing the linked list until the pointer of current node is the tail node.
            item = self.tail.data                               # stores current tail data
            self.tail = curr                                    # sets the tail node to the node before it
            self.tail.link = None                               # sets the pointer of the new tail node to 'None'
            return item                                         # returns the data that was store in the removed node