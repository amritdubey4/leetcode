# LeetCode 34. Find First and Last Position of Element in Sorted Array

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(left=True):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > target or (left and nums[mid] == target):
                    r = mid
                else:
                    l = mid + 1
            return l

        if not nums:
            return [-1, -1]
        left = find_bound(True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = find_bound(False) - 1
        return [left, right]
