# LeetCode 29. Divide Two Integers


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 2**31 - 1
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        a, b = abs(dividend), abs(divisor)
        res = 0
        while a >= b:
            shift = 0
            while a >= (b << shift):
                shift += 1
            shift -= 1
            res += 1 << shift
            a -= b << shift
        res *= sign
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res
