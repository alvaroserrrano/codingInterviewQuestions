"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
"""
from collections import Counter
class Solution:
    def containsDuplicate1(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return True
        return False
    def containsDuplicate2(self, nums):
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return True
        return False
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))
