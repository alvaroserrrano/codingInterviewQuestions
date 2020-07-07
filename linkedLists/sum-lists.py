'''
 you have 2 numbers represented by a linked list
 where each node contains a single digit. The digits
 are stored in reverse prder, such that the 1's digit
 is at the head of the list. Write a function that adds
 the 2 numbers and returns a linked list
'''

import unittest

def sum_list(num1, num2):
    node1, node2 = num1, num2
    carry = 0
    result_head, result_node = None, None
    while node1 or node2 or carry:
        value=carry
        if node1:
            value+= node1.data
            node1 = node1.next
        if node2:
            value += node2.data
            node2 = node2.next
        if result_node:
            result_node.next = Node(value % 10)
            result_node = result_node.next
        else:
            result_node = Node(value % 10)
            result_head = result_node
        carry = value / 10
    return result_head


class Node():
    def __init__(self, data, next=None):
        self.data, self.next=data, next

    def __str__(self):
        string = str(self.data)
        if self.next:
            string +=',' + str(self.next)
        return string

class Test(unittest.TestCase):
  def test_sum_list(self):
    num1 = Node(1,Node(2,Node(3)))
    num2 = Node(4,Node(9,Node(5)))
    self.assertEqual(str(sum_list(num1, num2)), "5,1,9")
    num1 = Node(9,Node(2,Node(3,Node(4,Node(1)))))
    num2 = Node(4,Node(9,Node(8)))
    self.assertEqual(str(sum_list(num1, num2)), "3,2,2,5,1")

if __name__ == "__main__":
  unittest.main()
