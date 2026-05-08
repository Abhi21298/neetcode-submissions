class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        l, r = 0, 1

        while l < r and r < len(prices):

            if prices[l] > prices[r]:
                l = r
                r = r + 1
            else:
                profit = max(profit, prices[r] - prices[l])
                r = r + 1

        return profit    
        
