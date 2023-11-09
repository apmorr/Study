def greedy(coinvalL, chang):
    coinvalL.sort()
    coinvalL.reverse()
    num = 0
    for c in coinvalL:
        num += chang // c
        chang = chang % c
    return num

print(greedy([1,5,10,25]), 63)      #outputs 6 coins
'''optimal'''

print(greedy([1,5,21,25]), 63)      #outputs 7 coins
'''not optimal'''