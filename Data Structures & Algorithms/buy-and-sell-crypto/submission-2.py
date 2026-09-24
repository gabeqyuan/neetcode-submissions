class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0 
        minBuy = prices[0]

        for sell in prices:
            maxprofit = max(maxprofit, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxprofit