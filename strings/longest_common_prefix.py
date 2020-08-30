"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
class Solution:
    def (self, strs):
        #empty list
        if not strs: return ""
        #only 1 word in the list
        if len(strs) == 1: return strs[0]
        strs.sort()
        prefix=''
        for x, y in zip(strs[0], strs[-1]):
            if x==y: prefix+=x
            else:break
        return prefix
