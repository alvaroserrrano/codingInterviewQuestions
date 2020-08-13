"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from collections import deque
class TreeNode(self, val=0, left=None, right=None):
    self.val=val
    self.left=left
    self.right=right
class Solution:
    def levelOrder(self, root):
        ans = []
        if root is None:
            return ans
        queue = []
        queue.append(root)
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                cur_node = queue.pop(0)
                level.append(cur_node.val)
                if cur_node.left is not None:
                    queue.append(cur_node.left)
                if cur_node.right is not None:
                    queue.append(cur_node.right)
            ans.append(level)
        return ans

