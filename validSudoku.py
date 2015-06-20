#########################################################################
## LeetCode Number 67 Valid Sudoku 
## Problem description can be found here:
## https://leetcode.com/problems/valid-sudoku/
## Python script
#########################################################################

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def checkList(self,array):
        storage = set()
        for item in array:
            if item != '.':
                if item in storage:
                    return 0
                else:
                    storage.add(item)
        return 1

    def isValidSudoku(self, board):
        result = 1
        column = ['.' for i in range(9)]
        for i in range(9):
            for j in range(9):
                column[i] += board[j][i]

        for i in range(9):
            result *= self.checkList(column[i])
            result *= self.checkList(board[i][:])
            if result==0:
                return False

        candidate = [[0,3],[3,6],[6,9]]
        for i in candidate:
            for j in candidate:
                here = []
                for m in range(i[0],i[1]):
                    here += board[m][j[0]:j[1]]
                print here
                if self.checkList(here) == 0:
                    return False

        return True
