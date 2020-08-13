"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBSTRecursion(self, root):
        def checkValid(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not checkValid(node.right, val, upper):
                return False
            if not checkValid(node.left, lower, val):
                return False
        return checkValid(root)
    def isValidBSTIteration(self, root):
        if root is None: return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper: return False
            stack.append((root.left, lower, val))
            stack.append((root.right, val, upper))
        return True
    def isValidBSTInOrderTraversal(self, root):
        stack = []
        inorder = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder: return False
            inorder = root.val
            root = root.right
        return True

