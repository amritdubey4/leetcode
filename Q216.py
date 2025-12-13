"""
LeetCode Q216: Combination Sum III
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
- Only numbers 1 through 9 are used.
- Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, 
and the combinations may be returned in any order.
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        
        def backtrack(start, remaining, path):
            if len(path) == k and remaining == 0:
                result.append(path[:])
                return
            
            if len(path) >= k or remaining < 0:
                return
            
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, remaining - i, path)
                path.pop()
        
        backtrack(1, n, [])
        return result

