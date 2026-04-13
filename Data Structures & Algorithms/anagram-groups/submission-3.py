class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            sort = ''.join(sorted(str))
            res[sort].append(str)
        return list(res.values())