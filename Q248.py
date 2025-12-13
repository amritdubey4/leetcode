"""
LeetCode Q248: Strobogrammatic Number III
Given two strings low and high that represent two integers low and high where low <= high, return the number of 
strobogrammatic numbers in the range [low, high].
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
"""

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
        
        def dfs(n, m):
            if n == 0:
                return ['']
            if n == 1:
                return ['0', '1', '8']
            
            result = []
            for num in dfs(n - 2, m):
                for left, right in pairs:
                    if n != m or left != '0':
                        result.append(left + num + right)
            
            return result
        
        def count(n):
            if n == 0:
                return 0
            if n == 1:
                return 3
            
            count = 4 * (5 ** ((n - 2) // 2))
            if n % 2 == 1:
                count *= 3
            else:
                count *= 1
            return count
        
        def generate_all(n):
            return dfs(n, n)
        
        low_num = int(low)
        high_num = int(high)
        result = 0
        
        for length in range(len(low), len(high) + 1):
            numbers = generate_all(length)
            for num in numbers:
                num_int = int(num)
                if low_num <= num_int <= high_num:
                    result += 1
        
        return result

