class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def back(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                return
            subset.append(nums[i])
            back(i + 1, subset)
            subset.pop()
            back(i + 1, subset)
        nums.sort()
        back(0, [])
        return [list(s) for s in res]