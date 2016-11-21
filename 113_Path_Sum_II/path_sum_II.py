# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res, stack = [], []
        if root:
            stack.append((root, [root.val]))
        while stack:
            node, val = stack.pop()
            if node.right:
                stack.append((node.right, val+[node.right.val]))
            if node.left:
                stack.append((node.left, val+[node.left.val]))
            if not node.right and not node.left and sum(val) == target:
                res.append(val)
        return res