#########################################################################
## LeetCode Number 103 Binary Tree Zigzag Level Order Traversal 
## Problem description can be found here:
## https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
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
    def zigzagLevelOrder(self, root):
        queue = []
        out = []
        level = []
        direction = 1

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
                if direction ==1:
                    direction = -1
                else:
                    level.reverse()
                    direction = 1
                out.append(level)
                if queue:
                    queue.append(None)
                level= []

        return out
