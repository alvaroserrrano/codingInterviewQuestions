"""Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []"""
class Solution:
    def three_sum(self, nums):
        #nlog(n) sorting to implement 2-pointer technique
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)):
            l = i+1
            r=len(nums) -1
            target= 0-nums[i]
            while l<r:
                if nums[l] + nums[r] == target:
                    ans.add((nums[l], nums[r], nums[i]))
                    l+=1
                    r-=1
                elif nums[l] + nums[r] > target: r-= 1
                else: l+= 1
        return list(ans)

sol = Solution()
print(sol.three_sum([-1,0,1,2,-1,-4]))
