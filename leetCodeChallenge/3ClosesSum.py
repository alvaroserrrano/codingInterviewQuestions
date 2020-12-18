"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        n = len(nums)
        for i in range(n):
            low, high = i+1, n-1
            while(low < high):
                sum = nums[i] + nums[low] + nums[high]
                if abs(target-sum) < diff:
                    diff = target-sum
                    if sum < target:
                        low += 1
                    else: high -= 1
            if diff == 0: break
        return target-diff

