"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution:
    def reverse1(self, x):
        ans = int(str(abs(x))[::-1])
        return (-ans if x < 0 else ans) if ans.bit_length() < 32 else 0
    def reverse2(self, x):
        max_int = pow(2, 31)-1
        min_int = pow(-2, 31)

        str_x = str(abs(x))
        rev_str_x = str_x[::-1]
        ans = int(rev_str_x)
        ans = ans * -1 if x < 0 else ans

        return ans if (ans < max_int and ans > min_int) else 0
