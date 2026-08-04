class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 1000
        maxprofit = 0
        for i in range(len(prices)):
            profit = prices[i]-minprice
            minprice = min(minprice, prices[i])
            maxprofit = max(profit, maxprofit)
        return maxprofit
        