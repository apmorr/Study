def insertion(L):
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j - 1] > L[j]:
            L[j], L[j - 1] = L[j-1], L[j]
            j -= 1

L = [3,6,1,9,2]
insertion(L)
print(L)


