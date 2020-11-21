"""

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution:
    def fourSum(self, nums, target):
        #this will work four 5Sum, 6Sum...
        #recursion until k == 2
        def kSum(nums, target, k):
            ans =[]
           #if sum of k smallest > target or sum of k largest < target, no need to continue checking
           if len(nums) == 0 or nums[0] * k > target or nums[-1]*k < target:
               return ans
           if k == 2: return twoSum(nums, target)
           #iterate through the array and skip duplicate values
           #recurse kSum with start=i+1, k=k-1, and target - nums[i]
           for i in range(len(nums)):
               if i == 0 or nums[i-1] != nums[i]:
                   for _, set in enumerate(kSum(nums[i+1:], target-nums[i], k-1)):
                       ans.append([nums[i]] + set)
            return ans


        def twoSum(nums, target):
            ans = []
            l, r = 0, len(nums)-1
            while(l < r):
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    ans.append(nums[l], nums[r])
                    l+=1
                    r-=1
            return ans
        nums=sorted(nums)
        return kSum(nums, target, 4)
