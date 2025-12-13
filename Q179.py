"""
LeetCode Q179: Largest Number
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.
"""

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(a, b):
            str_a = str(a)
            str_b = str(b)
            if str_a + str_b > str_b + str_a:
                return -1
            elif str_a + str_b < str_b + str_a:
                return 1
            else:
                return 0
        
        nums_sorted = sorted(nums, key=cmp_to_key(compare))
        
        if nums_sorted[0] == 0:
            return "0"
        
        return ''.join(map(str, nums_sorted))

