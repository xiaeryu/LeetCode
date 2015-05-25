#########################################################################
## LeetCode Number 176 Second Highest Salary
## Problem description can be found here:
## https://leetcode.com/problems/second-highest-salary/
## MySQL query statement
#########################################################################

Select MAX(Salary)
FROM Employee
WHERE Salary < (Select MAX(Salary) FROM Employee)
