"""
Given an array with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not supposed to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
def sortColors(arr):
    small, eq, large = 0, 0, len(arr) - 1
    while(eq <= large):
        if arr[eq] == 0:
            arr[small], arr[eq] = arr[eq], arr[small]
            small+=1
            eq+=1
        elif arr[eq] == 2:
            arr[eq], arr[large] = arr[large], arr[eq]
            large-=1
        else:
            eq+=1
    return arr

arr = [2, 0, 2, 1, 1, 0]
print(f' {arr} becomes {sortColors(arr)}')
