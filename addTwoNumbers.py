#########################################################################
## LeetCode Number 2 Add Two Numbers
## Problem description can be found here:
## https://leetcode.com/problems/add-two-numbers/
## Python script
#########################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        head = tmp = ListNode(0)
        flag = 0

        while l1 or l2 or flag:
            tmp1 = l1.val if l1 else 0
            tmp2 = l2.val if l2 else 0
            tmpSum = tmp1 + tmp2 + flag

            tmp.next = ListNode(tmpSum % 10)
            tmp = tmp.next
            flag = tmpSum / 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next
