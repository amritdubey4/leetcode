# LeetCode 47. Permutations II
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            prev = None
            for i in range(len(nums)):
                if used[i] or (prev is not None and nums[i] == prev):
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False
                prev = nums[i]

        backtrack([], [False] * len(nums))
        return res
