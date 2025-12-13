"""
LeetCode Q177: Nth Highest Salary
SQL Problem - Write a solution to find the nth highest salary from the Employee table. 
If there is no nth highest salary, return null.
"""

# SQL Solution (for MySQL):
# CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
# BEGIN
#   DECLARE M INT;
#   SET M = N - 1;
#   RETURN (
#     SELECT DISTINCT salary
#     FROM Employee
#     ORDER BY salary DESC
#     LIMIT 1 OFFSET M
#   );
# END

# Python solution for reference:
class Solution:
    def getNthHighestSalary(self, n: int, salaries: list[int]) -> int:
        unique_salaries = sorted(set(salaries), reverse=True)
        if n > len(unique_salaries):
            return None
        return unique_salaries[n - 1]

