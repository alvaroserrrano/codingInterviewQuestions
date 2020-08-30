"""
You have a list of integers, and for each index you want to find the product
of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list
of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

Python 3.6
your function would return:

  [84, 12, 28, 21]

Python 3.6
by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Python 3.6
Here's the catch: You can't use division in your solution!
"""

def get_products_of_all_ints_except_at_index(int_list):
    ans = [1] * len(int_list)
    left_prod = 1
    for i in range(len(int_list)):
        ans[i] *= left_prod
        left_prod *= int_list[i]
    right_prod = 1
    for i in reversed(range(len(int_list))):
        ans[i] *= right_prod
        right_prod *= int_list[i]
    return ans

print(get_products_of_all_ints_except_at_index([1, 7, 3, 4]))
# Tests

import unittest

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)
