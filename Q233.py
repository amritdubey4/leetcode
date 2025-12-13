"""
LeetCode Q233: Number of Digit One
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
"""

class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1
        
        while i <= n:
            divider = i * 10
            count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10
        
        return count

