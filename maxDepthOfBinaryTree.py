#########################################################################
## LeetCode Number 104 Maximum Depth of Binary Tree 
## Problem description can be found here:
## https://leetcode.com/problems/maximum-depth-of-binary-tree/
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
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) +1
