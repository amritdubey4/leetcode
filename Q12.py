# LeetCode 12. Integer to Roman


class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = []
        for v, s in zip(vals, syms):
            while num >= v:
                num -= v
                res.append(s)
        return "".join(res)
