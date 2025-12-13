"""
LeetCode Q186: Reverse Words in a String II
Given a character array s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Note: s may contain leading or trailing spaces or multiple spaces between two words. The returned string should 
only have a single space separating the words. Do not include any extra spaces.
"""

class Solution:
    def reverseWords(self, s: list[str]) -> None:
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        # Reverse entire string
        reverse(0, len(s) - 1)
        
        # Reverse each word
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                reverse(start, i - 1)
                start = i + 1
        reverse(start, len(s) - 1)

