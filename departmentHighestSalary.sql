#########################################################################
## LeetCode Number 184 Department Highest Salary
## Problem description can be found here:
## https://leetcode.com/problems/department-highest-salary/
## MySQL query statement
#########################################################################

# Write your MySQL query statement below
SELECT Department.Name AS Department, M.Name AS Employee, M.Salary AS Salary
FROM Department
JOIN
    (SELECT E.Name, E.Salary, E.DepartmentId
    FROM Employee E,
        (SELECT MAX(Salary) AS ms, DepartmentId
        FROM Employee
        GROUP BY DepartmentId) T
    WHERE E.Salary = T.ms
    AND E.DepartmentId = T.DepartmentId
        ) M
WHERE Department.Id = M.DepartmentId
