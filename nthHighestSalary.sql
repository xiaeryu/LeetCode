#########################################################################
## LeetCode Number 177 Nth Highest Salary
## Problem description can be found here:
## https://leetcode.com/problems/nth-highest-salary/
## MySQL query statement
#########################################################################

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT MAX(Salary)
      FROM Employee Emp1
      WHERE (N-1)=
      (
          SELECT COUNT(DISTINCT(Emp2.Salary))
          FROM Employee Emp2
          WHERE Emp2.Salary > Emp1.salary
      )
  );
END
