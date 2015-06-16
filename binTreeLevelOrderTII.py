#########################################################################
## LeetCode Number 107 Binary Tree Level Order Traversal II  
## Problem description can be found here:
## https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
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
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        queue = []
        out = []
        level = []

        if root:
            queue.append(root)
            queue.append(None)

        while queue:
            node = queue.pop(0)
            if node:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                out = [level] + out
                if queue:
                    queue.append(None)
                level= []

        return out
