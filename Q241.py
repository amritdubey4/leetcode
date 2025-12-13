"""
LeetCode Q241: Different Ways to Add Parentheses
Given a string expression of numbers and operators, return all possible results from computing all the different 
possible ways to group numbers and operators. You may return the answer in any order.
The test cases are generated such that the output values fit in a 32-bit integer and the number of different results 
does not exceed 104.
"""

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}
        
        def compute(left, right, op):
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            else:
                return left * right
        
        def dfs(expr):
            if expr in memo:
                return memo[expr]
            
            if expr.isdigit():
                return [int(expr)]
            
            result = []
            for i, char in enumerate(expr):
                if char in '+-*':
                    left_results = dfs(expr[:i])
                    right_results = dfs(expr[i + 1:])
                    
                    for left in left_results:
                        for right in right_results:
                            result.append(compute(left, right, char))
            
            memo[expr] = result
            return result
        
        return dfs(expression)

