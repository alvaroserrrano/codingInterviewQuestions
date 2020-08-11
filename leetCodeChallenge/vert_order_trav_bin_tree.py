"""
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively
will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the
vertical line touches some nodes, we report the values of the nodes in order
from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is
reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report
will have a list of values of nodes.

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
The node with value 5 and the node with value 6 have the same position
according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is
smaller than 6.
"""
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root):
        ans = collections.defaultdict(list)
        def helper(node, col, row):
            if not node:
                return
            ans[col].append((row, node.val))
            helper(node.left, row+1, col-1)
            helper(node.right, row+1, col+1)
        helper(root, 0, 0)
        ans = dict(sorted(ans.items()))
        res = []
        for k, v in ans.items():
            res.append([x[1] for x in sorted(v, key=lambda x:x)])
        return res

