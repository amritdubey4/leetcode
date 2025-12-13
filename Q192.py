"""
LeetCode Q192: Word Frequency
Write a bash script to calculate the frequency of each word in a text file words.txt.
For simplicity sake, you may assume:
- words.txt contains only lowercase characters and space ' ' characters.
- Each word must consist of lowercase characters only.
- Words are separated by one or more whitespace characters.
"""

# Bash Solution:
# cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{print $2, $1}'

# Python solution for reference:
class Solution:
    def wordFrequency(self, text: str) -> dict[str, int]:
        from collections import Counter
        words = text.split()
        return dict(Counter(words))

