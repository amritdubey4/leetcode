"""
LeetCode Q178: Rank Scores
SQL Problem - Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:
- The scores should be ranked from highest to lowest.
- If there is a tie between two scores, both should have the same ranking.
- After a tie, the next ranking number should be the next consecutive integer value.
"""

# SQL Solution:
# SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'
# FROM Scores
# ORDER BY score DESC


# Python solution for reference:
class Solution:
    def rankScores(self, scores: list[int]) -> list[tuple]:
        sorted_scores = sorted(set(scores), reverse=True)
        rank_map = {score: rank + 1 for rank, score in enumerate(sorted_scores)}
        result = [(score, rank_map[score]) for score in scores]
        return sorted(result, key=lambda x: x[0], reverse=True)
