    
import random

def coin_tosses():
    head_count = 0
    tails_count =0
    for result in range(1,5001):
        random_number=random.random()
        tosses= round(random_number)  
        tosses = tosses * 100
        result += 1
        if (tosses == 100):
            head_count += 1
            print "Attempt: #" + str(result)  + " Throwing a coin... it's " + "head(s)!" +  "... got " + str(head_count) + "so far"
        else:
            tails_count += 1
            print "Attempt: #" +str(result)  + " Throwing a coin... it's " +  "tail(s)!" + "... got " + str(tails_count) + "so far"
        if (result == 5000):
            print "Ending program. Thank you!"
coin_tosses()

