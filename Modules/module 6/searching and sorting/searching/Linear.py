def contains(L, item):  #runtime is O(n)
    for obj in L:
        if obj == item:
            return True
    return False

x = [1,5,2,7,6,8,3,4,89,0,2,4]
print(contains(x,5))

'''we can write the function more efficently'''

def contains_1(L, item):
    return any(obj == item for obj in L)

x = [1,5,2,7,6,8,3,4,89,0,2,4]
print(contains_1(x,3))
