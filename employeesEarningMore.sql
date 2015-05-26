#########################################################################
## LeetCode Number 181 Employees Earning More Than Their Managers
## Problem description can be found here:
## https://leetcode.com/problems/employees-earning-more-than-their-managers/
## MySQL query statement
#########################################################################

# Write your MySQL query statement below
SELECT Emp1.Name AS Employee
FROM Employee Emp1
LEFT JOIN Employee Emp2
ON Emp1.ManagerID = Emp2.Id
WHERE Emp1.Salary > Emp2.Salary
