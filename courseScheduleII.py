#########################################################################
## LeetCode Number 201 Course Schedule II  
## Problem description can be found here:
## https://leetcode.com/problems/course-schedule-ii/
## Python script
#########################################################################

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        if numCourses == 0:
            return []
        storage = [0] * numCourses
        cat = [[] for i in range(numCourses)]
        queue = []
        result = []

        for pair in prerequisites:
            storage[pair[0]] += 1
            cat[pair[1]].append(pair[0])

        for i in range(numCourses):
            if storage[i] == 0:
                queue.append(i)
                
        flag = True
        while flag and len(queue) > 0:
            get = queue.pop(0)
            storage[get] = -1
            result.append(get)
            for item in cat[get]:
                if storage[item] > 0:
                    storage[item] -= 1
                elif storage[item] == -1:
                    flag = False
                if storage[item] == 0:
                    queue.append(item)
                    
        if len(result) < numCourses:
            return []
        else:
            return result
