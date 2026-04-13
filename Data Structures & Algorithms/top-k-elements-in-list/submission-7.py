class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arr = []
        for num, i in count.items():
            arr.append([i, num])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res