"""
LeetCode Q130: Surrounded Regions
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board:
            return
        
        m, n = len(board), len(board[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            
            board[i][j] = 'T'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        # Mark border 'O's
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        
        # Flip remaining 'O's to 'X' and restore 'T's to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

