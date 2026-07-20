class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(amount):
            if amount in cache:
                return cache[amount]
            if amount == 0:
                return 0
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    cache[amount] = min(res, 1 + dfs(amount - coin))
                    res = cache[amount]
            return res
        return -1 if dfs(amount) >= 1e9 else dfs(amount)