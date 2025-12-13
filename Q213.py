"""
LeetCode Q213: House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two 
adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money 
you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        def rob_linear(houses):
            prev2 = houses[0]
            prev1 = max(houses[0], houses[1])
            
            for i in range(2, len(houses)):
                current = max(prev1, prev2 + houses[i])
                prev2 = prev1
                prev1 = current
            
            return prev1
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

