"""
Write a method that moves all zeros in an array to its end. You should maintain the order of
all other elements.
"""

#[1, 0, 2, 0, 4, 0] -> [1, 2 ,4, 0, 0, 0]
def zeros_to_end(nums):
    ins_pos = 0
    for num in nums:
        if num != 0:
            nums[ins_pos] = num
            ins_pos+= 1
    for i in range(ins_pos, len(nums)):
        nums[i] = 0
    return nums

nums = [1, 0, 2, 0, 4, 0]
print(zeros_to_end(nums))
