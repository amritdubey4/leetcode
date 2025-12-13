"""
LeetCode Q164: Maximum Gap
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. 
If the array contains less than two elements, return 0.
You must write an algorithm that runs in linear time and uses linear extra space.
"""

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0
        
        min_val, max_val = min(nums), max(nums)
        n = len(nums)
        
        if min_val == max_val:
            return 0
        
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        for num in nums:
            bucket_idx = (num - min_val) // bucket_size
            buckets[bucket_idx][0] = min(buckets[bucket_idx][0], num)
            buckets[bucket_idx][1] = max(buckets[bucket_idx][1], num)
        
        max_gap = 0
        prev_max = min_val
        
        for bucket in buckets:
            if bucket[0] == float('inf'):
                continue
            max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1]
        
        return max_gap

