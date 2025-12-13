"""
LeetCode Q161: One Edit Distance
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
A string s is said to be one distance apart from a string t if you can:
- Insert exactly one character into s to get t, or
- Delete exactly one character from s to get t, or
- Replace exactly one character of s with a different character to get t.
"""

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        
        if abs(m - n) > 1:
            return False
        
        if m > n:
            return self.isOneEditDistance(t, s)
        
        i = 0
        while i < m and s[i] == t[i]:
            i += 1
        
        if i == m:
            return m + 1 == n
        
        if m == n:
            i += 1
        
        while i < m and s[i] == t[i + 1]:
            i += 1
        
        return i == m

