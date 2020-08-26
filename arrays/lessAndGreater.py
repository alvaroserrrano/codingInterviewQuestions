"""
write a function that takes an array A of n numbers, and rearranges A’s
elements to get a new array B having the property that
B[0] ≤ B[1] ≥ B[2] ≤ B[3] ≥ B[4] ≤ B[5] ≥ · · · .
"""

#Time O(n) and no more than 2 elements in memory
def rearrange(nums):
    for i in range(len(nums)):
        if ((i & 1) == 0 and nums[i-1] < nums[i]) or ((i & 1) == 1 and nums[i-1] > nums[i]):
            nums[i-1], nums[i] = nums[i], nums[i-1]
    return nums


arr1 = [2, 4, 5, 6, 45, 3, 2, 1]
arr2= [5, 8, 7, 5, 3, 5, 3, 6, 3, 4]

print(rearrange(arr1))
print(rearrange(arr2))


"""
[1, 5, 4, 45, 3, 6, 2, 2]
[4, 8, 5, 7, 3, 5, 3, 6, 3, 5]
"""
