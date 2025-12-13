"""
LeetCode Q194: Transpose File
Given a text file file.txt, transpose its content.
You may assume that each row has the same number of columns, and each field is separated by the ' ' character.
"""

# Bash Solution:
# awk '{for(i=1;i<=NF;i++){if(NR==1){arr[i]=$i}else{arr[i]=arr[i]" "$i}}}END{for(i=1;i<=NF;i++)print arr[i]}' file.txt

# Python solution for reference:
class Solution:
    def transposeFile(self, lines: list[str]) -> list[str]:
        if not lines:
            return []
        
        rows = [line.split() for line in lines]
        num_cols = len(rows[0])
        transposed = []
        
        for col in range(num_cols):
            transposed.append(' '.join(row[col] for row in rows))
        
        return transposed

