class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)
        dp =[[0] for _ in range(n)]

        for length in range(1, n-1):
            for left in range(0, n-1-length):
                right = left + 1 +length
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right], nums[left]*nums[i]*nums[right]+dp[left][i]+dp[i][right])
        return dp[0][n-1]


