import collections
class Solution:
    def findDuplicates(self, nums):
        return [k for k, v in collections.Counter(nums).items() if v > 1]

sol = Solution()
print(sol.findDuplicates([2, 3, 4, 5, 6, 2, 3]))
