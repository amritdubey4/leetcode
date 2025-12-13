# LeetCode 38. Count and Say


class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            i = 0
            nxt = ""
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                nxt += str(j - i) + s[i]
                i = j
            s = nxt
        return s
