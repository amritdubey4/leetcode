"""
LeetCode Q244: Shortest Word Distance II
Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest 
distance between two different strings from the array.
Implement the WordDistance class:
- WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
- int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
"""

class WordDistance:
    def __init__(self, wordsDict: list[str]):
        self.word_indices = {}
        for i, word in enumerate(wordsDict):
            if word not in self.word_indices:
                self.word_indices[word] = []
            self.word_indices[word].append(i)
    
    def shortest(self, word1: str, word2: str) -> int:
        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]
        
        i = j = 0
        min_distance = float('inf')
        
        while i < len(indices1) and j < len(indices2):
            min_distance = min(min_distance, abs(indices1[i] - indices2[j]))
            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1
        
        return min_distance

