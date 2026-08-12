class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0 
        l, r = 0, 1
        while r <= n - 1:
            profit = prices[r] - prices[l]
            if profit <= 0:
                l = r
            else:
                max_profit = max(max_profit, profit)
            r += 1
        return max_profit


