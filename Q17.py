# LeetCode 17. Letter Combinations of a Phone Number
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = [""]
        for d in digits:
            res = [p + c for p in res for c in mapping.get(d, "")]
        return res
