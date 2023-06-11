from typing import List
class Solution:
    # ? Space complexity = O(n) 
    def maxProfit2(self, prices: List[int]) -> int:
        dp = {}
        dp[0] = prices[0]
        maxProf = 0
        for i in range(1, len(prices)):
            dp[i] = min(dp[i-1], prices[i])
            if prices[i] - dp[i] > maxProf:
                maxProf = prices[i] - dp[i]
        return maxProf
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        return max_profit
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        