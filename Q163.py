"""
LeetCode Q163: Missing Ranges
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are 
in the inclusive range.
A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
Return the smallest sorted list of ranges that cover every missing number exactly. 
That is, no element of nums is in any of the ranges, and each missing number is in exactly one of the ranges.
"""

class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        result = []
        prev = lower - 1
        
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            
            if prev + 1 <= curr - 1:
                if prev + 1 == curr - 1:
                    result.append(str(prev + 1))
                else:
                    result.append(str(prev + 1) + "->" + str(curr - 1))
            
            prev = curr
        
        return result

