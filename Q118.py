"""
LeetCode Q118: Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        
        triangle = [[1]]
        
        for i in range(1, numRows):
            row = [1]
            prev_row = triangle[i - 1]
            
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            
            row.append(1)
            triangle.append(row)
        
        return triangle

