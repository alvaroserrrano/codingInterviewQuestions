"""
Write an efficient function that checks whether any permutation  of an input
string is a palindrome. ↴

You can assume the input string only contains lowercase letters.

Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
"But 'ivicc' isn't a palindrome!"

If you had this thought, read the question again carefully. We're asking if
any permutation of the string is a palindrome. Spend some extra time ensuring
you fully understand the question before starting. Jumping in with a flawed
understanding of the problem doesn't look good in an interview.
"""

def has_palindrome_permutation(string):
    counter = {}
    odd_count = 0
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    for count in counter.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count <= 1

import unittest


# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
