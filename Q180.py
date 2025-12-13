"""
LeetCode Q180: Consecutive Numbers
SQL Problem - Write a solution to find all numbers that appear at least three times consecutively.
Return the result table in any order.
"""

# SQL Solution:
# SELECT DISTINCT l1.num AS ConsecutiveNums
# FROM Logs l1
# JOIN Logs l2 ON l1.id = l2.id - 1 AND l1.num = l2.num
# JOIN Logs l3 ON l1.id = l3.id - 2 AND l1.num = l3.num

# Python solution for reference:
class Solution:
    def consecutiveNumbers(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums) - 2):
            if nums[i] == nums[i + 1] == nums[i + 2]:
                if nums[i] not in result:
                    result.append(nums[i])
        return result

