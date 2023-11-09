def mergesort(L):
    # base case!
    if len(L) < 2:  # if the list has less than two values, the merge sort wont work so the code exits
        return L

    # Divide!
    mid = len(L)//2 # assigns a value to half of the length of the list
    A = L[:mid]     # assigns A to the first half of the list
    B = L[mid:]     # assigns B to second half of list

    # Conquer!
    mergesort(A)    # recalls function
    mergesort(B)    # recalls function

    # Combine!
    merge(A, B, L)  # calls merge and with the lists as parameters

def merge(A, B, L):
    i = 0 # index into A
    j = 0 # index into B
    while i < len(A) and j < len(B):    # while A and B both have elements in their list, this loop continues
        if A[i] < B[j]:                 # compares to see if the first value of the A list is less that the first value of teh B list
            L[i+j] = A[i]               # if it is, it adds the indexes together to find what index in L the value should be place
            i = i + 1
        else:
            L[i+j] = B[j]
            j = j+1
    # add any remaining elements once one list is empty
    L[i+j:] = A[i:] + B[j:]