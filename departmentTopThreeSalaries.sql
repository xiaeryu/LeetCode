#########################################################################
## LeetCode Number 185 Department Top Three Salaries 
## Problem description can be found here:
## https://leetcode.com/problems/department-top-three-salaries/
## MySQL query statement
#########################################################################

## Failed to make this out myself & extract the code from the forum.

# Write your MySQL query statement below
SELECT D.Name AS Department, E.Name AS Employee, E.Salary AS Salary 
FROM Employee E, Department D
WHERE 
    (SELECT COUNT(DISTINCT(Salary))
    FROM Employee
    WHERE DepartmentId = E.DepartmentId 
    AND Salary > E.Salary) < 3
AND E.DepartmentId = D.Id 
ORDER by E.DepartmentId, E.Salary DESC;
