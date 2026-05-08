class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            profit = sell - minBuy
            maxP = max(maxP, profit)
            minBuy = min(minBuy, sell)
        return maxP