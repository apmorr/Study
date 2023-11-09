def fib_memo(k, fib_array):
    if k in [0,1]:
        fib_array[k] = k
        return fib_array[k]
    if fib_array[k] != None:
        return fib_array[k]
    fib_array[k] = fib_memo(k-1, fib_array) + fib_memo(k-2, fib_array)
    return fib_array[k]

k = 2
fib_array = [None]*(k+1)
print(fib_memo(k, fib_array))