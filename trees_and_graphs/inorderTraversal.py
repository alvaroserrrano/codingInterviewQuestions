class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def helper(root, ans):
        if root is not None:
            if root.left is not None:
                helper(root.left, ans)
            ans.append(root.val)
            if root.right is not None:
                helper(root.right, ans)
    def inorder(root):
        ans = []
        helper(root, ans)
        return ans

