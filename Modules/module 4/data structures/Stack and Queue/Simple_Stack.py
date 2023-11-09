stack = []          ##creates a Stack using a list
stack.append(10)    ##adds elements to the end of the Stack
stack.append(20)
stack.append(30)

print(stack)        ##returns our stack(list)
stack.pop()         ##returns the last element in the stack(list) and removes it
stack.pop()
stack.pop()
#stack.pop()        ##the stack(list) is empty so it returns a error

#-----------------------------------------------------------------------------------#

stack = []
print(len(stack) == 0)     ##checks if stack(list) is empty, returs True if it is
print(not stack)           ##another way to check if stack is empty, returns True if stack is empty

stack.append(10)
stack.append(20)

print(stack[-1])            ##returns the element in the index of -1,
'''returns 20'''            ##in a list, the index of -1 is always the last element in the list no matter the length


