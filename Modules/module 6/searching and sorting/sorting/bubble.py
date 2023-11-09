def bubble_sort(L): #runtime O(n^2)
    for iterator in range(len(L)-1):
        for i in range(len(L)-1-iterator):
            if L[i] > L[i+1]: #If two items are out of order
                L[i], L[i+1] = L[i+1], L[i] #Switch them
L2 = [5,4,3,2,1]
bubble_sort(L2)