"""
LeetCode Q89: Gray Code
An n-bit gray code sequence is a sequence of 2n integers where:
- Every integer is in the inclusive range [0, 2n - 1],
- The first integer is 0,
- An integer appears at most once in the sequence,
- The binary representation of every pair of adjacent integers differs by exactly one bit, and
- The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.
"""

class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = [0]
        
        for i in range(n):
            size = len(result)
            for j in range(size - 1, -1, -1):
                result.append(result[j] | (1 << i))
        
        return result

