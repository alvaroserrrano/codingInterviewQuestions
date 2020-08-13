"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
class ListNode:
    def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solutions:
    def mergeTwoLists1(self, l1, l2):
        head = cur =ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next
        #copy remaining elements
    def mergeTwoListsRecursively(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        elif l1.val < l2.val:
            l1.next = self.mergeTwoListsRecursively(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecursively(l1, l2.next)
            return l2

