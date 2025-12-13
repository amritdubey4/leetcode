"""
LeetCode Q126: Word Ladder II
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words 
beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord is not a wordList.
- sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences 
from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list 
of the words [beginWord, s1, s2, ..., sk].
"""

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        from collections import defaultdict, deque
        
        if endWord not in wordList:
            return []
        
        wordList = set(wordList)
        wordList.add(beginWord)
        
        # Build adjacency graph
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                graph[pattern].append(word)
        
        # BFS to find shortest paths
        parents = defaultdict(set)
        distance = {beginWord: 0}
        queue = deque([beginWord])
        
        while queue:
            current = queue.popleft()
            
            if current == endWord:
                break
            
            for i in range(len(current)):
                pattern = current[:i] + '*' + current[i+1:]
                for neighbor in graph[pattern]:
                    if neighbor not in distance:
                        distance[neighbor] = distance[current] + 1
                        parents[neighbor].add(current)
                        queue.append(neighbor)
                    elif distance[neighbor] == distance[current] + 1:
                        parents[neighbor].add(current)
        
        # DFS to build paths
        result = []
        
        def build_paths(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            
            for parent in parents[word]:
                build_paths(parent, path + [parent])
        
        if endWord in parents or beginWord == endWord:
            build_paths(endWord, [endWord])
        
        return result

