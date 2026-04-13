class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            if target - n in indices and indices[target - n] != i:
                return [indices[target - n], i]
            indices[n] = i
        return []