'''the amount of time to run a algorith depend on software, hardware, environment,
 and the implementation of the algorithm itself'''

'''using time functions, we can take the start time, then run the algorithm, then take the end time
 and subtract from the start time to get the total time it took for the algorithm to complete'''

import time

start_time = time, time()  # sets to variable to the numbers of seconds passed since epoch
###code you wish to time###         #epoch is just a specific point in time that is consitent, unchanging and a good standard
end_time = time.time()  # sets the variable to the new amount of seconds since epoch
total_time = end_time - start_time  # the difference between the two times is how long it took for the algorith to run

'''tracking how long your algorithm takes to run can help you better optimize your work
if it takes too long to run you know you probably should focus on that portion of code and remove any reduntent code'''

'''the any() function returns True if at least one element of an iterable is True'''

i = [0, False, 5]
print(any(i))  ##True since 5 is true

j = [0, False]
print(any(j))  ## False sinceall elements are false

'''using built in functions like this can reduce redundant code and optimize the efficiency of your work'''


def duplicates2(L):     '''removes redundant code from duplicates_1 so it runs faster'''
    n = len(L)
    for i in range(1,n):
        for j in range(i):

            if L[i] == L[j]:
                return True
    return False

def duplicates3(L):  '''reduces duplicates2 into 2 lines to drastically reduce run time and redundancy'''
    n = len(L)
    return(any(L[i] == L[j] for i in range (1,n) for j in range(i)))

'''measuring time is a good way to measure preformance and efficency of a algorithm, but it may not always be the most reliable way'''


























