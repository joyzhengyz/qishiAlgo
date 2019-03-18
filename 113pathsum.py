# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    if not root:
        return []
    res = []
    #Stack LIFO
    stack = [(root, sum-root.val, [root.val])]
    while stack:
        curr, val, ls = stack.pop()
        if not curr.left and not curr.right and val == 0:
            res.append(ls)
        if curr.right:
            stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
        if curr.left:
            stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
    return res