"""
You've built an inflight entertainment system with on-demand movie streaming.

Users on longer flights like to start a second movie right when their first
one ends, but they complain that the plane usually lands before they can see
the ending. So you're building a feature for choosing two movies whose total
runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list
of integers movie_lengths (in minutes) and returns a boolean indicating whether
there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory
"""

def can_two_movies_fill_flight(movie_lengths, flight_length):
    if len(movie_lengths) == 0: return False
    ans = dict()
    ans[movie_lengths[0]] = 0
    for i in range(1, len(movie_lengths)):
        second_movie_len = flight_length - movie_lengths[i]
        if second_movie_len in ans:
            return True
        else:
            ans[movie_lengths[i]] = i
    return False

import unittest

# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = can_two_movies_fill_flight([4, 3, 2], 5)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)
