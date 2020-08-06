"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
#linear time and no extra space(we return the output arr)
"""
the idea is to move every item to its 'best' position.
For example, if we find a 4, its index will be (4-1) 3
We will keep a flag on every index to determine if we have seen that value
in the array before
Since 1 <= a[i] <= n, our flag will be to mark that index as negative
In the end, all negative indexes will be returned in an output array
"""
class Solution:
    def findDuplicates(self, nums):
        ans = []
        for i, num in enumerate(nums):
            idx = abs(num) - 1
            if nums[idx] < 0: ans.append(idx+1)
            nums[idx] = -nums[idx]
        return ans
    import collections

    #one liner solution
    def findDuplicates_one_liner(self, nums):
        return [k for k, v in collections.Counter(nums).items() if v > 1]

    #make duplicate numbers positive
    def findDuplicates3(self, nums):
        ans = []
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] *= -1
            if (nums[abs(nums[i])-1] > 0):
                ans.append(abs(nums[i]))
        return ans

l1 = [4,3,2,7,8,2,3,1]
l2 = [3, 3, 5, 6, 7, 4, 9]
l3 = [1, 2, 3, 4, 5, 6]
sol = Solution()
print(f'{l1} -> 2 and 3 are expected and returned val is {sol.findDuplicates(l1)}')
print(f'{l2} -> 3 is expected and returned val is {sol.findDuplicates(l2)}')
print(f'{l3} -> [] is expected and returned val is {sol.findDuplicates(l3)}')
