#########################################################################
## LeetCode Number 207 Course Schedule  
## Problem description can be found here:
## https://leetcode.com/problems/course-schedule/
## Python script
#########################################################################

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        if numCourses == 0:
            return True
        storage = [0] * numCourses
        cat = [[] for i in range(numCourses)]
        queue = []
        visited = 0

        for pair in prerequisites:
            storage[pair[0]] += 1
            cat[pair[1]].append(pair[0])

        for i in range(numCourses):
            if storage[i] == 0:
                queue.append(i)

        while len(queue) > 0:
            get = queue.pop(0)
            visited += 1
            storage[get] = -1
            for item in cat[get]:
                if storage[item] > 0:
                    storage[item] -= 1
                elif storage[item] == -1:
                    return False
                if storage[item] == 0:
                    queue.append(item)
        return visited==numCourses
