"""
A tree is “superbalanced” if the difference between the depths of any two leaf nodes ↴ is no greater than one.
"""
class TreeNode(self, value):
    self.value = value;
    self.right  = None;
    self.left = None

    def insert_left(self, value):
        self.left = TreeNode(value)
        return self.left

    def insert_right(value):
        self.right = TreeNode(value)
        return self.right

    def is_superbalanced(root):
        if root is None: return True
        depths = []
        nodes = []
        nodes.append((root, 0))

        while(len(nodes)):
            node, depth = nodes.pop()
            #if we reach a leaf
            if(not node.left) and (not node.right):
                #check if depth is present in our array
                if depth not in depths:
                    depths.append(depth)
                    #check for imbalance
                    #case 1 -> more than 2 different depths
                    if((len(depths) > 2)): return False
                    #case 2 -> difference between depths is more than one
                    if(len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                        return False
                else:
                    if node.left:
                        nodes.append((node.left, depth + 1))
                    if node.right:
                        nodes.append((node.right, depth + 1))
        return True
