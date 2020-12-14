"""
The aim to partition the string into all possible palindrome combinations. To achieve this, we must generate all possible substrings of a string by partitioning at every index until we reach the end of the string. Example, abba can be partitioned as ["a","ab","abb","abba"]. Each generated substring is considered as a potential candidate if it a Palindrome.
"""

class Solution:
    def partition(self, s):
        def isPalindrome(s):
            if not s: return False
            return s == s[::-1]
        ans = []
        if not s:
            return []
        #if the string in the param is a palindrome itself
        if isPalindrome(s):
            word = [s]
            ans.append(word)
        #otherwise
        n = len(s)
        for i in range(n):
            if isPalindrome(s[:i]):
                prefix = [s[:i]]
                #append prefix to partitions
                remaining = [prefix + word for word in self.partition(s[i:])]
                ans += remaining
        return and


