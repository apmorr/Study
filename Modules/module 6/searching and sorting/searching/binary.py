def BS(L, item):    #runtime is O(n)
    if len(L) == 0:
        return False
    mid_index = len(L) // 2
    if item == L[mid_index]:
        return True
    elif item < L[mid_index]:
        return BS(L[ : mid_index], item)
    else:
        return BS(L[mid_index + 1 : ], item)