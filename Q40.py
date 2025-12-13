# LeetCode 40. Combination Sum II
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            prev = None
            for i in range(start, len(candidates)):
                if prev is not None and candidates[i] == prev:
                    continue
                prev = candidates[i]
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res
