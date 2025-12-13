"""
LeetCode Q243: Shortest Word Distance
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, 
return the shortest distance between these two words in the list.
"""

class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        index1 = index2 = -1
        min_distance = float('inf')
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                index1 = i
                if index2 != -1:
                    min_distance = min(min_distance, abs(index1 - index2))
            elif word == word2:
                index2 = i
                if index1 != -1:
                    min_distance = min(min_distance, abs(index1 - index2))
        
        return min_distance

