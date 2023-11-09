def f(k):
    if k > 0:
        return f(k-1) + k
    return 0

print(f(5))

