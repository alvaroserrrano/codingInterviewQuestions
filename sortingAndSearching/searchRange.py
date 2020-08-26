"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9
"""
class Solution:
    #find point where left and right indices intersect
    def doBinSearch(self, nums, target, isLeft):
        left = 0
        right = len(nums)
        while (left < right):
            middle = (left + right) // 2
            if nums[middle] > target or (isLeft and target == nums[middle]):
                right = middle
            else:
                left = middle + 1
        return left
    #log(n) time
    def searchReange(self, nums, target):
        #use bool flag where True searches for left and False for right
        left_index = self.doBinSearch(nums, target, True)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        right_index= self.doBinSearch(nums, target, False) -1
        return(left_index, right_index)



