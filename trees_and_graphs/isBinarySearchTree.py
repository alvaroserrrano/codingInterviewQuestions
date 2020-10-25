"""
Write a function to check that a binary tree is a valid binary tree
"""

def __init__(self, value):
    self.value = value
    self.left  = None
    self.right = None

def insert_left(self, value):
    self.left = BinaryTreeNode(value)
    return self.left

def insert_right(self, value):
    self.right = BinaryTreeNode(value)
    return self.right

def isBinarySearchTreeWithStack(root):
    stack = [(root, -float('inf'), float('inf'))]

    #DFS
    while(len(stack)):
        node, low_bound, up_bound = stack.pop()
        if (node.val <= low_bound) or (node.val >= up_bound):
            return False
        if node.left:
            stack.append((node.left, low_bound, node.value))
        if node.right:
            stack.append((node.right, node,value, up_bound))

    return True

def isBinarySearchTreeRecursive(root, low_bound=-float('inf')m up_bound=float('inf')):
    if not root: return True
    if (root.val <= low_bound) or (node.val >= up_bound): return False
    return (isBinarySearchTreeRecursive(root.left, low_bound, root.value) and isBinarySearchTreeRecursive(root.right, root.value, up_bound))



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
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)
