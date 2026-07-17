class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        residx, reslen = 0, 0
        cache = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or cache[i + 1][j - 1]):
                    cache[i][j] = True
                    if j - i + 1 > reslen:
                        residx = i
                        reslen = j - i + 1
        return s[residx : residx + reslen]