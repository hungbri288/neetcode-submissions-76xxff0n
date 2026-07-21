class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dfs(i):
            if cache[i] != -1:
                return cache[i]
            LIS = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))
            cache[i] = LIS
            return cache[i]
        return max(dfs(i) for i in range(len(nums)))