"""
LeetCode Q249: Group Shifted Strings
We can shift a string by shifting each of its letters to its successive letter.
For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.
For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.
"""

class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        from collections import defaultdict
        
        def get_key(s):
            if not s:
                return ""
            key = []
            base = ord(s[0])
            for char in s:
                diff = (ord(char) - base) % 26
                key.append(str(diff))
            return ",".join(key)
        
        groups = defaultdict(list)
        for s in strings:
            groups[get_key(s)].append(s)
        
        return list(groups.values())

