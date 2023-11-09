def duplicates_1(L):                        #takes in a List of numbers
    n = len(L)                              #sets n to the length of the list
    for i in range(n):                      #loops the same number of times as the length of the list (if length is 50, will loop 50 times)
        for j in range(n):                  #loops the same number of times as the length of the list
                                                ##after each time i loops to a new number, j loops through all the possible numbers first
            if i != j and L[i] == L[j]:     #if i and j are not the same but the values at their respective indexes are, it will return true
                return True
    return False                            #returns false if no duplicates

def duplicates2(L):
    n = len(L)
    for i in range(1,n):
        for j in range(i):

            if L[i] == L[j]:
                return True
    return False

def duplicates3(L):
    n = len(L)
    return any(L[i] == L[j] for i in range (1, n) for j in range(i))

if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 6, 7, 8]
    assert(duplicates_1(L))

    L = [1, 2, 3, 4]
    assert(not duplicates_1(L))
