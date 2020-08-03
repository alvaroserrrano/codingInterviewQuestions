"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
class Solution:
     def invertTree(self, root: TreeNode) -> TreeNode:
         stack = [root]
         while stack:
             node = stack.pop(-1)
             if node:
                 #swap
                 node.left, node.right = node.right, node.left
                 stack.append(node.left)
                 stack.append(node.right)
        return root

