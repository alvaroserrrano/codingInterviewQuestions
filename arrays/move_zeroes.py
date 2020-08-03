"""
The 2 requirements of the question are:

Move all the 0's to the end of array.

All the non-zero elements must retain their original order.

Example
Input : [0, 1, 0, 3, 12]
Output : [1, 3, 12, 0, 0]

It's good to realize here that both the requirements are mutually exclusive,
i.e., you can solve the individual sub-problems and then combine them for the
final solution.
"""
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        for num in range(len(nums)):
            if nums[num] != 0:
                nums[ptr] = nums[num]
                ptr += 1
        for num in range(ptr, len(nums) - 1):
            nums[num] = 0

