import unittest

import unittest

def get_permutations(str):
    if len(str) <= 1:
        return set([str])
    all_chars_except_last = str[:-1]
    last_char=str[-1]
    permutations_except_last_char=get_permutations(all_chars_except_last)
    permutations = set()
    for permutation in permutations_except_last_char:
        for index in range(len(all_chars_except_last) +1):
            permutation = (permutations_except_last_char[:index]
                           + last_char + permutations_except_last_char[index:])
            permutations.add(permutation)
    return permutations

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
