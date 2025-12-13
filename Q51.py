"""
LeetCode Q51: N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def is_safe(row, col, board):
            # Check column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check diagonal \
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check diagonal /
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row, board):
            if row == n:
                result.append(["".join(row) for row in board])
                return

            for col in range(n):
                if is_safe(row, col, board):
                    board[row][col] = "Q"
                    backtrack(row + 1, board)
                    board[row][col] = "."

        result = []
        board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(0, board)
        return result
