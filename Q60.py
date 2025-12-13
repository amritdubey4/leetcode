"""
LeetCode Q60: Permutation Sequence
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123", "132", "213", "231", "312", "321"
Given n and k, return the kth permutation sequence.
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        
        numbers = list(range(1, n + 1))
        result = []
        k -= 1  # Convert to 0-indexed
        
        for i in range(n - 1, -1, -1):
            fact = factorial(i)
            index = k // fact
            result.append(str(numbers[index]))
            numbers.pop(index)
            k %= fact
        
        return ''.join(result)

