"""
LeetCode Q65: Valid Number
A valid number can be split up into these components (in order):
1. A decimal number or an integer.
2. (Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):
1. (Optional) A sign character (either '+' or '-').
2. One of the following formats:
   - One or more digits, followed by a dot '.'.
   - One or more digits, followed by a dot '.', followed by one or more digits.
   - A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):
1. (Optional) A sign character (either '+' or '-').
2. One or more digits.
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        
        seen_digit = False
        seen_dot = False
        seen_e = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif char in ['e', 'E']:
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False
            elif char in ['+', '-']:
                if i != 0 and s[i - 1] not in ['e', 'E']:
                    return False
            else:
                return False
        
        return seen_digit

