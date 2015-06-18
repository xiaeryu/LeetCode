#########################################################################
## LeetCode Number 112 Path Sum 
## Problem description can be found here:
## https://leetcode.com/problems/path-sum/
## Python script
#########################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if (not root.left) and (not root.right):
            if root.val == sum:
                return True
            else:
                return False
        
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
