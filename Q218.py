"""
LeetCode Q218: The Skyline Problem
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. 
Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:
- lefti is the x coordinate of the left edge of the ith building.
- righti is the x coordinate of the right edge of the ith building.
- heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
"""

import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))
        
        events.sort()
        
        result = []
        heap = [(0, float('inf'))]
        removed = {}
        
        for x, neg_height, right in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            
            if neg_height != 0:
                heapq.heappush(heap, (neg_height, right))
            
            if not result or result[-1][1] != -heap[0][0]:
                result.append([x, -heap[0][0]])
        
        return result

