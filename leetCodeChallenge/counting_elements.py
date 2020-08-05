"""
Given an integer array arr count element x such that x+1 is also in arr
If there is duplicated in arr, count them separately

Example 1:
input: arr=[1, 2, 3]
output: 2
explanation: 1 and 2 are counted because 2 and 3 are in the array

Example 2:
input: arr = [1, 1, 3, 3, 5, 5, 7, 7]
output: 0
explanation: no numbers are counted becase 2, 4, 6, and 8 are not present
"""
import collections
class Solution:
    def countElements(self, arr):
        count = 0
        for num in arr:
            if num + 1 in arr:
                count += 1
        return count
    def countElements_2(self, arr):
        counts = collections.Counter(arr)
        return sum(counts[num] for num in counts if num+1 in counts)
if __name__ == "__main__":
    sol = Solution()
    print(sol.countElements([1,2,3]))
    print(sol.countElements([1,1,3,3,5,5,7,7]))
    print(sol.countElements([1,3,2,3,5,0]))
    print(sol.countElements([1,1,2,2]))

    print(sol.countElements_2([1,2,3]))
    print(sol.countElements_2([1,1,3,3,5,5,7,7]))
    print(sol.countElements_2([1,3,2,3,5,0]))
    print(sol.countElements_2([1,1,2,2]))
