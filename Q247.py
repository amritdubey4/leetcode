"""
LeetCode Q247: Strobogrammatic Number II
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
"""

class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
        
        def dfs(n, m):
            if n == 0:
                return ['']
            if n == 1:
                return ['0', '1', '8']
            
            result = []
            for num in dfs(n - 2, m):
                for left, right in pairs:
                    if n != m or left != '0':
                        result.append(left + num + right)
            
            return result
        
        return dfs(n, n)

