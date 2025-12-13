"""
LeetCode Q52: N-Queens II
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(row, col, board):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True
        
        def backtrack(row, board):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                if is_safe(row, col, board):
                    board[row][col] = 'Q'
                    count += backtrack(row + 1, board)
                    board[row][col] = '.'
            
            return count
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        return backtrack(0, board)

