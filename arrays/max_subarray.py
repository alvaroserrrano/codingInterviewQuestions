
"""
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        temp = 0
        max_so_far = nums[0]
        for i in range(0, len(nums)):
            temp = max(nums[i], temp + nums[i])
            if temp > max_so_far:
                max_so_far = temp
        return max_so_far
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
