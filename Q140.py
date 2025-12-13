"""
LeetCode Q140: Word Break II
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word 
is a valid dictionary word. Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        memo = {}
        
        def backtrack(start):
            if start == len(s):
                return [""]
            
            if start in memo:
                return memo[start]
            
            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    substrings = backtrack(end)
                    for substring in substrings:
                        if substring:
                            result.append(word + " " + substring)
                        else:
                            result.append(word)
            
            memo[start] = result
            return result
        
        return backtrack(0)

