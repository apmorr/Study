def ss_min(L):
    for i in range(len(L) - 1):
        min = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min]:
                min = j

        L[i], L[min] = L[min], L[i]