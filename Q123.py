"""
LeetCode Q123: Best Time to Buy and Sell Stock III
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0
        
        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
        
        return sell2

