#########################################################################
## LeetCode Number 144 Binary Tree Preorder Traversal  
## Problem description can be found here:
## https://leetcode.com/problems/binary-tree-preorder-traversal/
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
    # @return {integer[]}
    def preorderTraversal(self, root):
        storage = []
        if root:
            storage = [root.val]
            storage = storage + self.preorderTraversal(root.left)
            storage = storage + self.preorderTraversal(root.right)
        else:
            storage = []
        return storage
