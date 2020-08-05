"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""
class Solution(object):
    def isPowerOfFour(self, num):
        while(num % 4 == 0 and num > 0):
            num = num/4
        if num == 1:
            return True
        return False
