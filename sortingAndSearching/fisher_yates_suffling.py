"""
Write a function for doing an in-place ↴ shuffle of a list.

The shuffle must be “uniform,” meaning each item in the original list must have the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.
"""
import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

#picks a random element from the list and puts it in the first index
#once an element is placed at an index it cannot be moved from there
def shuffle(the_list):
    # Shuffle the input in place
    if len(the_list) <= 1: return the_list
    last_index = len(the_list) -1
    #O(n) time and O(1) space
    for index in range(0, len(the_list) -1):
        #choose random element from available (not placed yet)
        element_index=get_random(index, last_index)
        #place random element in index by swapping
        if index != element_index:
            the_list[index], the_list[element_index] = the_list[element_index], the_list[index]





sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)
