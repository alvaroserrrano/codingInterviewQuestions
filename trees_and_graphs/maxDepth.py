"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepthOneLiner(self, root):
        return 1 + max(self.maxDepthOneLiner(root.left), self.maxDepthOneLiner(root.right)) if root else 0
    def maxDepth(self, root):
        #BFS
        depth = 0
        queue = [root] if root else []
        while queue:
            depth += 1
            tempQueue = []
            for el in queue:
                if el.left:
                    tempQueue.append(el.left)
                if el.right:
                    tempQueue.append(el.right)
            queue = tempQueue
        return depth
