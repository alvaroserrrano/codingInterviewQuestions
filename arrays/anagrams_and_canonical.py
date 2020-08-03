"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for str in strs:
            ans[tuple(sorted(str))].append(str)
        return ans.values()

#O(nk(logk)) time
#O(n) space
