"""
LeetCode Q245: Shortest Word Distance III
Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, 
return the shortest distance between these two words in the list.
Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.
"""

class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        index1 = index2 = -1
        min_distance = float('inf')
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                if word1 == word2 and index1 != -1:
                    min_distance = min(min_distance, i - index1)
                index1 = i
                if index2 != -1 and word1 != word2:
                    min_distance = min(min_distance, abs(index1 - index2))
            elif word == word2:
                index2 = i
                if index1 != -1:
                    min_distance = min(min_distance, abs(index1 - index2))
        
        return min_distance

