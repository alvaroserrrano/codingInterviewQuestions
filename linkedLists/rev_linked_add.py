"""
You are given 2 non empty linked lists representing 2 non-negative
integers . The digits are stored in reverse order and each of
their nodes contain a single digit. Add the 2 numbers and
return a linked list with the digits in reverse order

Example:
Input ( 2 -> 4 -> 3 ) + (5 -> 6 ->4)
Output (7 ->0 -> 8)
342 + 465 = 807
"""

#1. pointer for each input list

#2. add 2 pointer

#3. if sum >=10 set carry flag to true and add 1

#4. advance pointers

#5. once boht pointers reach the end, check for a carry and add one if necessary

class Solution:
    def add_two_numbers(self, l1: ListNode, l2 : ListNode) -> ListNode:
        c = 0
        result = l1.val + l2.val + c
        c = result // 10
        ret =result % 10
        if(l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.add_two_numbers(l1.next, l2.next, c)
        return ret


