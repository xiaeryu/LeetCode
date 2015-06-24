#########################################################################
## LeetCode Number 67 Binary Tree Postorder Traversal 
## Problem description can be found here:
## https://leetcode.com/problems/binary-tree-postorder-traversal/
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
    def postorderTraversal(self, root):
        if not root:
            return []
        output = []
        output.extend(self.postorderTraversal(root.left))
        output.extend(self.postorderTraversal(root.right))
        output.append(root.val)
        
        return output
