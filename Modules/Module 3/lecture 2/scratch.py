                 ###asymptotic analysis###

'''atomic operations are what we are gonn  use to determine the cost of an algorithm'''

'''the atomic operations are as follows:
        -arithmetic and boolean operations
        -variable assignment
        -branching
        -calling a function
        -returning from a function: 'return x' 
        
        remember to count operations not lines of code'''


'''assign each operation a cost'''
'''count the total cost'''
def f001(L):
    newlist = []                    #2 - create, assign
    for i in L:                     #n - loops times:
        if i % 2 == 0:              #2 - arithmetic, compare
            newlist.append(i)       #1 - append
    return newlist                  #1 - return

                            #2 + n(2 + 1) + 1 = 3n + 3

def sum_calc(k):
    total = 0                       #1 - assignment
    for i in range(1, k+1):         #k - loops times
        total += i                  #1 - arithmetic, assignment
    return total                    #1 - return
                                    #1 + k*1 + 1 = k + 2

def sum_clever(k):
    total = k*(k+1)//2              #3 - mathematic
    return total                    #1 - assignment
                                    #1 - return
                                    #1 + 1 + 3 = 5

#1 - assignment
#n loops times
    #n loops times
        #2 - arithmetic, compare
            #1 - return
#1 - return
#2 + n(n(2)) + 1 = 2n^2 + 3











