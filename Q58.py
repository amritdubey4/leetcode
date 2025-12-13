"""
LeetCode Q58: Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        if not s:
            return 0
        
        last_space = s.rfind(' ')
        if last_space == -1:
            return len(s)
        
        return len(s) - last_space - 1

