"""
Check if a tree is a binary search tree
"""



#     self.left=None
#     self.right=None

#     def insert_left(self, value):
#         self.left = TreeNode(value)
#         return self.left

#     def insert_right(self, value):
#         self.right=TreeNode(value)
#         return self.right

def check_binary_search_tree(root):
    #keep track and compare Node value to lower and upper bound
    temp = [(root, -float('inf'), float('inf'))]
    while(len(temp)):
        node, lower, upper = temp.pop()
        if(node.value <= lower) or (node.value >= upper):
            return False
        if node.left:
            temp.append((node.left, lower, node.value))
        if node.right:
            temp.append((node.right, node.value, upper))
    return True

import unittest

# Tests

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = check_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = check_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = check_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = check_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = check_binary_search_tree(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)
