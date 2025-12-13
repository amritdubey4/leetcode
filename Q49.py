# LeetCode 49. Group Anagrams
from typing import List, Dict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d: Dict[str, List[str]] = {}
        for s in strs:
            key = "".join(sorted(s))
            d.setdefault(key, []).append(s)
        return list(d.values())
