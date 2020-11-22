"""
You’re working with an intern that keeps coming to you with JavaScript code that won’t run because the braces, brackets, and parentheses are off. To save you both some time, you decide to write a braces/brackets/parentheses validator.

Let’s say:

‘(’, ‘{’, ‘[’ are called " openers ."
‘)’, ‘}’, ‘]’ are called " closers ."
Write an efficient function that tells us whether or not an input string’s openers and closers are properly nested.

Examples:

“{ [ ] ( ) }” should return True
“{ [ ( ] ) }” should return False
“{ [ }” should return False
Gotchas
Simply making sure each opener has a corresponding closer is not enough —we must also confirm that they are correctly ordered .

For example, “{ [ ( ] ) }” should return False, even though each opener can be matched to a closer.

We can do this in O(n)O(n) time and space. One iteration is all we need!

Breakdown
"""


import unittest

def is_valid(code):
    my_struct = {
        '(' : ')',
        '{' : '}',
        '[' : ']',
    }
    openers = set(my_struct.keys())
    closers = set(my_struct.values())

    my_stack = []
    for char in code:
        if char in openers:
            my_stack.append(char)
        elif char in closers:
            if not  my_stack:
                return False
            else:
                if char != my_struct[my_stack.pop()]: return False
    return my_stack == [] #True when stack is empty


# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)
