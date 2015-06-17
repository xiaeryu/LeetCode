#########################################################################
## LeetCode Number 94 Binary Tree Inorder Traversal 
## Problem description can be found here:
## https://leetcode.com/problems/binary-tree-inorder-traversal/
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
    def inorderTraversal(self, root):
        if root:
            storage=[root.val]
            if root.left:
                storage = self.inorderTraversal(root.left) + storage
            if root.right:
                storage = storage + self.inorderTraversal(root.right)
        else :
            storage=[]
        return storage
