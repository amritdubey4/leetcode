"""
LeetCode Q185: Department Top Three Salaries
SQL Problem - Write a solution to find the employees who are high earners in each of the departments.
A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
Return the result table in any order.
"""

# SQL Solution:
# SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
# FROM Employee e
# JOIN Department d ON e.departmentId = d.id
# WHERE (
#     SELECT COUNT(DISTINCT e2.salary)
#     FROM Employee e2
#     WHERE e2.departmentId = e.departmentId AND e2.salary > e.salary
# ) < 3

# Python solution for reference:
class Solution:
    def departmentTopThreeSalaries(self, employees: list[dict], departments: list[dict]) -> list[dict]:
        dept_salaries = {}
        for emp in employees:
            dept_id = emp['departmentId']
            if dept_id not in dept_salaries:
                dept_salaries[dept_id] = []
            dept_salaries[dept_id].append(emp['salary'])
        
        dept_top3 = {}
        for dept_id, salaries in dept_salaries.items():
            unique_salaries = sorted(set(salaries), reverse=True)[:3]
            dept_top3[dept_id] = set(unique_salaries)
        
        dept_map = {dept['id']: dept['name'] for dept in departments}
        result = []
        for emp in employees:
            if emp['salary'] in dept_top3[emp['departmentId']]:
                result.append({
                    'Department': dept_map[emp['departmentId']],
                    'Employee': emp['name'],
                    'Salary': emp['salary']
                })
        return result

