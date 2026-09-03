class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}     #dp = {(i, buy) : res}
        def dec(i, buy):
            if i == len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            res = dec(i + 1, buy)
            if buy:
                res = max(res, + dec(i + 1, False) + prices[i])
            else:
                res = max(res, dec(i + 1, True) - prices[i])
            dp[(i, buy)] = res
            return res
        return dec(0, False)