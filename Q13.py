# LeetCode 13. Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and vals[s[i]] < vals[s[i + 1]]:
                res += vals[s[i + 1]] - vals[s[i]]
                i += 2
            else:
                res += vals[s[i]]
                i += 1
        return res
