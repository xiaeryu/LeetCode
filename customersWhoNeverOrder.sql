#########################################################################
## LeetCode Number 183 Customers Who Never Order
## Problem description can be found here:
## https://leetcode.com/problems/customers-who-never-order/
## MySQL query statement
#########################################################################

# Write your MySQL query statement below
SELECT Name
FROM Customers
LEFT JOIN(
    SELECT CustomerId, COUNT(CustomerId) AS ct
    FROM Orders
    GROUP BY CustomerId
) T
ON Customers.Id = T.CustomerId
WHERE ct IS NULL
