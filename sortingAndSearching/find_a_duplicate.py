"""
Find a duplicate, Space Edition™.

We have a list of integers, where:

The integers are in the range 1..n1..n
The list has a length of n+1n+1
It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.

Write a function which finds an integer that appears more than once in our list. (If there are multiple duplicates, you only need to find one of them.)

We're going to run this function on our new, super-hip MacBook Pro With Retina Display™. Thing is, the damn thing came with the RAM soldered right to the motherboard, so we can't upgrade our RAM. So we need to optimize for space!
"""

#O(nlog(n)) time and O(1) space without destroying input
#using an auxiliary set would require O(n) space
#brute force involves 2 nested loops O(n^2) time
#sorting the list takes O(nlog(n)) time and duplicates will appear next to each other but that takes O(n) space to store the sorted list
#the goal is to do an in-place sort and return the number as soon as a duplicate is found
#we divide input list in 2 sublists
#sublist 1= [0, n/2]
#sublist 2=[n/2 +1, n-1]
#sum of the sublists must be 1 greater than the sum of the sublists' distinct possibilities
#one of the sublists must have at least one more element than it has possible distinct integers
#once we find that sublist we will iterate recursively until we just have 1 item on range
#binary search dividing range of possibilities in half, not input list
def find_repeat(numbers):
    left=1
    right = len(numbers) - 1
    while(left < right):
        #divide into lower and upper ranges using middle point
        middle = left + ((right - left) // 2)
        lower_range_left, lower_range_right = left, middle
        upper_range_left, upper_range_right = middle + 1, right
        numbers_in_lower = 0
        for num in numbers:
            if num >= lower_range_left and num <= lower_range_right:
                numbers_in_lower += 1
        #compare numbers in lower range to the actual possible number of distinct numbers in that range
        possible_distinct_numbers_in_lower = (lower_range_right - lower_range_left + 1)
        if numbers_in_lower > possible_distinct_numbers_in_lower:
            left, right = lower_range_left, lower_range_right
        else:
            #check upper range
            left, right = upper_range_left, upper_range_right
    #left and right have converged and they point  to the same number
    return left

print(f'Result for [4, 1, 4, 8, 3, 2, 7, 6, 5] is',find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5]))
print(f'Result for [1, 2, 5, 5, 5, 5] is', find_repeat([1, 2, 5, 5, 5, 5]))
print(f'Result for [1, 2, 3, 2] is', find_repeat([1, 2, 3, 2]))

import unittest
# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
