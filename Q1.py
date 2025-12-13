# LeetCode 1. Two Sum
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            j = seen.get(target - n)
            if j is not None:
                return [j, i]
            seen[n] = i
