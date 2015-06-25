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
        storage = [[] for i in range(numCourses)]
        visit = [0 for i in range(numCourses)]
        for pair in prerequisites:
            storage[pair[0]].append(pair[1])
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in storage[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
