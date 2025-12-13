"""
LeetCode Q214: Shortest Palindrome
You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.
"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        n = len(combined)
        lps = [0] * n
        
        length = 0
        i = 1
        
        while i < n:
            if combined[i] == combined[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        longest_palindrome = lps[-1]
        return rev_s[:len(s) - longest_palindrome] + s

