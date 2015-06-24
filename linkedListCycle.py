#########################################################################
## LeetCode Number 141 Linked List Cycle 
## Problem description can be found here:
## https://leetcode.com/problems/linked-list-cycle/
## Python script
#########################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head:
            go = back = head
            while go and go.next and go.next.next and back and back.next:
                go = go.next.next
                back = back.next
                if go == back:
                    return True
        return False
