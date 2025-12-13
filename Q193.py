"""
LeetCode Q193: Valid Phone Numbers
Given a text file file.txt that contains a list of phone numbers (one per line), write a one-liner bash script 
to print all valid phone numbers.
You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. 
(x means a digit)
You may also assume each line in the text file must not contain leading or trailing white spaces.
"""

# Bash Solution:
# grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt

# Python solution for reference:
import re

class Solution:
    def validPhoneNumbers(self, lines: list[str]) -> list[str]:
        pattern = r'^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$'
        return [line.strip() for line in lines if re.match(pattern, line.strip())]

