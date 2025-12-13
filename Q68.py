"""
LeetCode Q68: Text Justification
Given an array of strings words and a width maxWidth, format the text such that each line has exactly 
maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line 
does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.
"""

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        i = 0
        
        while i < len(words):
            line_words = []
            line_length = 0
            
            # Collect words for current line
            while i < len(words):
                word = words[i]
                if line_length + len(word) + len(line_words) <= maxWidth:
                    line_words.append(word)
                    line_length += len(word)
                    i += 1
                else:
                    break
            
            # Build the line
            if i == len(words) or len(line_words) == 1:
                # Last line or single word: left justify
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                # Distribute spaces evenly
                total_spaces = maxWidth - line_length
                gaps = len(line_words) - 1
                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                
                line = line_words[0]
                for j in range(1, len(line_words)):
                    spaces = spaces_per_gap + (1 if j <= extra_spaces else 0)
                    line += ' ' * spaces + line_words[j]
            
            result.append(line)
        
        return result

