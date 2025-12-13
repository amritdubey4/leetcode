"""
LeetCode Q184: Department Highest Salary
SQL Problem - Write a solution to find employees who have the highest salary in each of the departments.
Return the result table in any order.
"""

# SQL Solution:
# SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
# FROM Employee e
# JOIN Department d ON e.departmentId = d.id
# WHERE (e.departmentId, e.salary) IN (
#     SELECT departmentId, MAX(salary)
#     FROM Employee
#     GROUP BY departmentId
# )

# Python solution for reference:
class Solution:
    def departmentHighestSalary(self, employees: list[dict], departments: list[dict]) -> list[dict]:
        dept_max_salary = {}
        for emp in employees:
            dept_id = emp['departmentId']
            if dept_id not in dept_max_salary or emp['salary'] > dept_max_salary[dept_id]:
                dept_max_salary[dept_id] = emp['salary']
        
        dept_map = {dept['id']: dept['name'] for dept in departments}
        result = []
        for emp in employees:
            if emp['salary'] == dept_max_salary[emp['departmentId']]:
                result.append({
                    'Department': dept_map[emp['departmentId']],
                    'Employee': emp['name'],
                    'Salary': emp['salary']
                })
        return result

