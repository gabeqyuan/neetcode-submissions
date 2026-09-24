class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0

        buy = 0
        sell = 1

        while sell <= len(prices) - 1:
            if prices[buy] >= prices[sell]:
                buy = sell
                sell = buy + 1
                continue 
            else:
                profit = prices[sell] - prices[buy]
                maxprofit = max(profit, maxprofit)
                sell+= 1
            






        return maxprofit 