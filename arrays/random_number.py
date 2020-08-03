"""
Given a list of ranges, return a random number that' s present within one of
the ranges. Every  number has the same probability to be chosen
"""
import random

def get_random(list):
    total = 0
    ans = 0
    for range in list:
        total +=  range[1] - range[0] + 1
    temp = random.randint(0, total-1)
    for range in list:
        single_range = range[1] - range [0] + 1
        #fits within range
        if temp <  single_range:
            ans = range[0] + temp
            break
        #random num is bigger than single range, move on to the next range
        else:
            temp -= single_range
    return ans

print('Random number from list of ranges is: ',get_random([[12, 15], [1, 5], [32, 34]]))
