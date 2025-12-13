"""
LeetCode Q176: Second Highest Salary
SQL Problem - Write a solution to find the second highest distinct salary from the Employee table. 
If there is no second highest salary, return null.
"""

# SQL Solution:
# SELECT MAX(salary) AS secondHighestSalary
# FROM Employee
# WHERE salary < (SELECT MAX(salary) FROM Employee)

