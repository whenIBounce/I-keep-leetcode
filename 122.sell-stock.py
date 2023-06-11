from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = 0 - prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[i][0]          

test_cases = [
    [7,1,5,3,6,4], # Expected output: 5
    [7,6,4,3,1], # Expected output: 0
    [1,2,3,4,5], # Expected output: 4
    [1], # Expected output: 0
    [2, 1], 
    [1, 2]
]

solution = Solution()

for i, prices in enumerate(test_cases):
    print(f"Test case {i+1}:")
    print("Input:", prices)
    print("Output:", solution.maxProfit(prices))
    print()
