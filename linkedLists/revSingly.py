"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
class Node(self, val = 0, next = None):
    self.val = val
    self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        cur = head
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev=cur
            cur=temp
        return prev
"""
input [1,2,3,4,5]
output[5,4,3,2,1]
"""
