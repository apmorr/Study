import time                                                         #imports time functions
from duplicates import duplicates_1                                 #imports the duplicates_1 function from the duplicates file

def timetrials(dup, n, trials = 10):
    total_time = 0                                                  #local varaible that will be manipulated
    for i in range(trials):                                         #loops the amount of time the 'trials' parameter is set to (default is 10)
        start_time = time.time()                                    #creates and sets start time as the current time
        dup(list(range(n)))                                         #creates a list with the n parameter, then calls the duplicate_1 function and passes in the new created list
        end_time = time.time()                                      #creates a variable to hold the time after the duplicate_1 function has ran
        total_time += end_time - start_time                         #sets total time to the amount of time inbetween the start and end time, plus the prev total_time
    print("average = %0.7f for n = %d" % (total_time/trials, n))    #prints the average time it took for each value of n passed in

print("Running duplicates_1 programg")
for n in [50, 100, 200, 400, 800, 1600, 3200]:
    timetrials(duplicates_1, n)                                     #calls the time trial function and passes in the duplicate_1 function and a value of n