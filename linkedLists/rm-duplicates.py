#remove duplicates from a linked list
import unittest

class Node():
    def __init__(self, val, next):
        self.val = val
        self.next = next

def rm_duplicates(head):
    node = head
    if node:
        values = {node.val: True}
        while node.next:
            if node.next.val in values:
                node.next = node.next.next
            else:
                values[node.next.val] = True
                node = node.next
    return head

class Test(unittest.TestCase):
    def test_rm_dups(self):
        head = Node(1, Node(3, Node(3, Node(1, Node(5, None)))))
        rm_duplicates(head)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 3)
        self.assertEqual(head.next.next.val, 5)
        self.assertEqual(head.next.next.next, None)

if __name__ == "__main__":
    unittest.main()
