"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
class Node(self, val = 0, next= None):
    self.val = val
    self.next = next
class Solution:
    #O(n)time and space
    def isPalindrome(self, head):
        ans = []
        while head:
            ans += head.val
            head = head.next
        return ans == ans[::-1]
    #O(n) time and O(1) space
