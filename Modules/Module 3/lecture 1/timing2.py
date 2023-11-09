import time
from duplicates import duplicates_1

n = 1000
for i in range(5):
    start_time = time.time()
    duplicates_1(list(range(n)))
    end_time = time.time()
    timetaken = end_time - start_time

    print("Time taken for n = ", n, ": ", timetaken)