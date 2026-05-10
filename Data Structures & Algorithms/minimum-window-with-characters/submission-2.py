class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, current = {}, {}
        l, formed = 0, 0
        best_len = len(s) + 1
        best_l = 0
        for i in range(len(t)):
            need[t[i]] = 1 + need.get(t[i], 0)
        for r in range(len(s)):
            current[s[r]] = 1 + current.get(s[r], 0)
            if s[r] in need and need[s[r]] == current[s[r]]:
                formed += 1
                while formed == len(need):
                    left = s[l]
                    current[left] -= 1
                    if r - l + 1 < best_len:
                        best_len = r - l + 1
                        best_l = l
                    if left in need and current[left] < need[left]:
                        formed -= 1

                    l += 1
        if best_len == len(s) + 1:
            return ""
        return s[best_l : best_l + best_len]