"""
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for
which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.
"""
class Solution(object):
    def isHappy(self, n):
        visited = set()
        def do_proc(num):
            res = 0
            while num > 0:
                digit = num % 10
                res += digit * digit
                num = num // 10
            return res
        while do_proc(n) not in visited:
            sum = do_proc(n)
            if sum == 1:
                return True
            visited.add(sum)
            n = sum
        return False
