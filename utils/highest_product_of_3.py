"""
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
"""

#O(n) time using greedy algorithm
def highest_product_of_3(nums):
    if len(nums) < 3: raise ValueError('Lenght of input list must be greater than or equal to 3')
    highest_product_of_3 = nums[0] * nums[1] * nums[2]
    highest_product_of_2 = nums[0] * nums[1]
    lowest_product_of_2 = nums[0] * nums[1]
    highest_num = max(nums[0], nums[1])
    lowest_num = min(nums[0], nums[1])
    for i in range(2, len(nums)):
        current = nums[i]
        highest_product_of_3 = max(highest_product_of_3, current * highest_product_of_2, current * lowest_product_of_2)
        highest_product_of_2 = max(highest_product_of_2, current * highest_num, current * lowest_num)
        lowest_product_of_2 = min(lowest_product_of_2, current * highest_num, current * lowest_num)
        highest_num = max(highest_num, current)
        lowest_num = min(lowest_num, current)
    return highest_product_of_3

import unittest
# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
