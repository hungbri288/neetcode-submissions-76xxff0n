class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        total = sum(nums)
        target = total // 2
        n = len(nums)
        cache = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, target):
            if target == 0:
                return True
            if i == n or target < 0:
                return False
            if cache[i][target] != -1:
                return cache[i][target]
            cache[i][target] = (dfs(i + 1, target) or dfs(i + 1, target - nums[i]))

            return cache[i][target]
        return dfs(0, target)