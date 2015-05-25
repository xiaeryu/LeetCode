
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
