"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.
"""
from collections import deque
class TreeNode(self, val=0, left=None , righ=None):
    self.val=val
    self.left = left
    self.right=right
class Solution:
    #O(n) time and O(n) space determined by height of the tree
    def isSymmetricRecursively(self, root):
        def areMirrors(t1, t2):
            if t1 is None and t2 is None: return True
            if t1 is None or t2 is None: return False
            return (t1.val == t2.val) and areMirrors(t1.left, t2.right) and areMirrors(t1.right, t2.left)
        return (areMirrors(root, root))
    def isSymmetricIteratively(self, root):
        if not root: return True
        queue = collections.deque([(root.left, root.left)])
        while queue:
            l, r = queue.pop()
            if l is None and r is None: continue
            if l is None or r is None: return False
            if l.val != r.val: return False
            queue.append((l.left, r.right))
            queue.append((l.right, r.left))
        return True
