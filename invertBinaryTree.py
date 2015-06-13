#########################################################################
## LeetCode Number 226 Invert Binary Tree
## Problem description can be found here:
## https://leetcode.com/problems/invert-binary-tree/
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
    # @return {TreeNode}
    def invertTree(self, root):
        if root:
            tmp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(tmp)
        return root
