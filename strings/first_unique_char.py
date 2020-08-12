"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.


Note: You may assume the string contains only lowercase English letters.
"""
from collections import Counter
class Solution:
    def firstUniqueChar(self, s):
        c = Counter(s)
        for i, letter in enumerate(s):
            if c[letter] == 1: return i
        return -1
