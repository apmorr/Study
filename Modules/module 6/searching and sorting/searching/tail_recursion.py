def bs_iterative(array, x, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = (low + high)//2
        if array[mid] == x:
            return mid #return the index of the element
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return - 1



def bs_rec(array, x, low, high):
    if low <= high:
        mid = (low + high)//2
        if array[mid] == x:
            return mid #return the index of the element
        elif array[mid] < x:
            return bs_rec(array, x, mid + 1, high)
        else:
            return bs_rec(array, x, low, mid - 1)
    else: return -1