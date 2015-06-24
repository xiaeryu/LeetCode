#########################################################################
## LeetCode Number 98 Validate Binary Search Tree
## Problem description can be found here:
## https://leetcode.com/problems/validate-binary-search-tree/
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
    # @return {boolean}
    def Traversal(self, root):
        storage = []
        if root:
            storage.extend(self.Traversal(root.left))
            storage.append(root.val)
            storage.extend(self.Traversal(root.right))
        return storage

    def isValidBST(self, root):
        array = self.Traversal(root)
        for i in range(1,len(array)):
            if array[i] <= array[i-1]:
                return False
        return True
