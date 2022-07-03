# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        current_max = 0
        
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            if prices[i] - min_price > current_max:
                current_max = prices[i] - min_price
            
        return current_max
