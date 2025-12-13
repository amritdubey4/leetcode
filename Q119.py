"""
LeetCode Q119: Pascal's Triangle II
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        
        for i in range(rowIndex):
            new_row = [1]
            for j in range(len(row) - 1):
                new_row.append(row[j] + row[j + 1])
            new_row.append(1)
            row = new_row
        
        return row

