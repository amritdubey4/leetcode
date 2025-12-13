"""
LeetCode Q195: Tenth Line
Given a text file file.txt, print just the 10th line of the file.
If the file has less than 10 lines, print nothing.
"""

# Bash Solution:
# sed -n '10p' file.txt
# OR
# awk 'NR==10' file.txt

# Python solution for reference:
class Solution:
    def tenthLine(self, lines: list[str]) -> str:
        if len(lines) < 10:
            return ""
        return lines[9]

