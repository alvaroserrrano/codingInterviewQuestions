"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array.

Example:

Input: [1,3,5,6], 5
Output: 2
Input: [1,3,5,6], 2
Output: 1
"""
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            middle = left + (right-left) // 2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle + 1
        return left
