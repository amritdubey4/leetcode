"""
LeetCode Q152: Maximum Product Subarray
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, 
and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        max_prod = min_prod = result = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])
            
            result = max(result, max_prod)
        
        return result

