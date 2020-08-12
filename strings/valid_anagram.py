"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution:
    def isAnagram1(self, s, t):
        return sorted(s) == sorted(t)
    def isAnagram2(self, s, t):
        d1 , d2 = {}, {}
        for i in s:
            d1[i] = d1.get(i, 0) + 1
        for i in t:
            d2[i] = d2.get(i, 0) + 1
        return d1==d2
    def isAnagram3(self, s, t):
        d1, d2 = [0]*26, [0]*26
        for i in s.lower():
            d1[ord(i)-ord('a')] += 1
        for i in t.lower():
            d2[ord(i)-ord('a')] += 1
        return d1 == d2
