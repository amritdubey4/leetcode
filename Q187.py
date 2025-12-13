"""
LeetCode Q187: Repeated DNA Sequences
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur 
more than once in a DNA molecule. You may return the answer in any order.
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 10:
            return []
        
        seen = set()
        repeated = set()
        
        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            if substring in seen:
                repeated.add(substring)
            seen.add(substring)
        
        return list(repeated)

