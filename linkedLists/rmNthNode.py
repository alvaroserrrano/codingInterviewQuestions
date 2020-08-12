"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next= next
class Solution:
    def removeNthFromEnd(self, head, n):
        cur = Node()
        len = 0
        cur.next = head
        first = head
        while(first != None):
            len += 1
            first = first.next
        len -= n
        first = cur
        while(len > 0):
            len-=1
            first = first.next
        first.next = first.next.next
        return cur.next
"""
input [1, 2, 3, 4, 5], 2
output [1, 2, 3, 5]
"""
