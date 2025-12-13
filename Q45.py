# LeetCode 45. Jump Game II
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        cur_end = 0
        cur_far = 0
        for i in range(len(nums) - 1):
            cur_far = max(cur_far, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = cur_far
        return jumps
