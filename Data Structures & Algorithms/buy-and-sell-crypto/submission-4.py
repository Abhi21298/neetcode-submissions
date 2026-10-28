class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices or len(prices) <= 1:
            return 0

        l, r = 0, 1
        profit = 0

        while r < len(prices):

            if prices[l] > prices[r]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])
            
            r += 1
        
        return profit
        
            

        