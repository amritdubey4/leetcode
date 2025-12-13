"""
LeetCode Q181: Employees Earning More Than Their Managers
SQL Problem - Write a solution to find the employees who earn more than their managers.
Return the result table in any order.
"""

# SQL Solution:
# SELECT e1.name AS Employee
# FROM Employee e1
# JOIN Employee e2 ON e1.managerId = e2.id
# WHERE e1.salary > e2.salary

# Python solution for reference:
class Solution:
    def employeesEarningMore(self, employees: list[dict]) -> list[str]:
        result = []
        manager_map = {emp['id']: emp['salary'] for emp in employees}
        
        for emp in employees:
            if emp.get('managerId') and emp['salary'] > manager_map.get(emp['managerId'], 0):
                result.append(emp['name'])
        
        return result

