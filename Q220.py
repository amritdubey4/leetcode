"""
LeetCode Q220: Contains Duplicate III
You are given an integer array nums and two integers indexDiff and valueDiff.
Find a pair of indices (i, j) such that:
- i != j,
- abs(i - j) <= indexDiff.
- abs(nums[i] - nums[j]) <= valueDiff.
Return true if such pair exists or false otherwise.
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        
        buckets = {}
        bucket_size = valueDiff + 1
        
        for i, num in enumerate(nums):
            bucket_id = num // bucket_size
            
            if bucket_id in buckets:
                return True
            
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            
            buckets[bucket_id] = num
            
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // bucket_size]
        
        return False

