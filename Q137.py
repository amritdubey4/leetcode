"""
LeetCode Q137: Single Number II
Given an integer array nums where every element appears three times except for one, which appears exactly once. 
Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        
        return ones

