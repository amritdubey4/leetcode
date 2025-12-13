# LeetCode 37. Sudoku Solver
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empties.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)

        def backtrack(idx=0):
            if idx == len(empties):
                return True
            r, c = empties[idx]
            b = (r // 3) * 3 + c // 3
            for d in "123456789":
                if d not in rows[r] and d not in cols[c] and d not in boxes[b]:
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[b].add(d)
                    if backtrack(idx + 1):
                        return True
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[b].remove(d)
                    board[r][c] = "."
            return False

        backtrack()
