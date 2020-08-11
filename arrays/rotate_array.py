"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

class Solution():
    #Time-> O(n * k)
    #O(1) space
    def rotateBruteForce(self, nums, k):
        k %= len(nums)
        for i in range(k):
            previous = nums[-1]
            #swap
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]

    #O(n) time and space
    def rotateExtraSpace(self, nums, k):
        temp = [0] * len(nums)
        for i in range(len(nums)):
            arr[(k + i) % len(nums)] = nums[i]
        nums[:] = temp

    def rotateCyclic(self, nums, k):
        n = len(nums)
        k %= n
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1

"""
input ([1, 2, 3, 4, 5, 6, 7], 3)
output [5, 6, 7, 1, 2, 3, 4]
"""
