# LeetCode 30. Substring with Concatenation of All Words
from typing import List, Dict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        target = {}
        for w in words:
            target[w] = target.get(w, 0) + 1
        res = []
        for i in range(0, len(s) - total_len + 1):
            seen = {}
            j = 0
            while j < num_words:
                word = s[i + j * word_len : i + (j + 1) * word_len]
                if word not in target:
                    break
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > target[word]:
                    break
                j += 1
            if j == num_words:
                res.append(i)
        return res
