#########################################################################
## LeetCode Number 19 Remove Nth Node From End of List
## Problem description can be found here:
## https://leetcode.com/problems/add-binary/
## Python script
#########################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        front = back = head
        for i in range(n):
            front = front.next
        if not front:
            head = head.next
            return head
        while(front.next):
            front = front.next
            back = back.next
        tmp = back.next
        back.next = tmp.next
    
        return head
