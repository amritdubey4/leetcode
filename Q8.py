# LeetCode 8. String to Integer (atoi)


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        # skip leading spaces
        while i < n and s[i] == " ":
            i += 1
        sign = 1
        if i < n and s[i] in ("+", "-"):
            if s[i] == "-":
                sign = -1
            i += 1
        res = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            res = res * 10 + digit
            i += 1
        return sign * res
