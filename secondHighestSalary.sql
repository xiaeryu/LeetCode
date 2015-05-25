Select MAX(Salary)
FROM Employee
WHERE Salary < (Select MAX(Salary) FROM Employee)
