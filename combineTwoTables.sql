#########################################################################
## LeetCode Number 175 Combine Two Tables
## Problem description can be found here:
## https://leetcode.com/problems/combine-two-tables/
## MySQL query statement
#########################################################################

SELECT Person.FirstName, Person.LastName, Address.City, Address.State
FROM Person
LEFT JOIN Address
ON Person.PersonId=Address.PersonId
