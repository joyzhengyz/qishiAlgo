class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def levelOrder(self,root):
        res = []
        if not root:
            return res
        q = []
        q.append(root)
        while q:
            n = len(q)
            print n,q[0].val,q[1].val
            level = []
            for i in range(n):
                t = q[0]
                q.pop(0)
                level.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(level)
        return res

    def levelOrder2(self, root):
        res, level = [], [root]
        while root and level:
            # append root value
            res.append([node.val for node in level])
            left_right_pair = [(node.left, node.right) for node in level]
            level = [leaf for LR in left_right_pair for leaf in LR if leaf]
        return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print TreeNode(root).levelOrder2(root)