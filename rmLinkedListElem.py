#########################################################################
## LeetCode Number 203 Remove Linked List Elements 
## Problem description can be found here:
## https://leetcode.com/problems/remove-linked-list-elements/
## Python script
#########################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        while head:
            if head.val == val:
                prev.next = head.next
                head = prev
            prev = head
            head = head.next
        return dummy.next
