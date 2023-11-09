def quicksort(l):
    # base case
    if len(l) < 2:
        return l

    # divide
    pivot = l[-1]
    lt = [e for e in l if e < pivot]
    et = [e for e in l if e == pivot]
    gt = [e for e in l if e > pivot]

    # conquer
    A = quicksort(lt)
    B = quicksort(gt)

    # combine
    return A + et + B