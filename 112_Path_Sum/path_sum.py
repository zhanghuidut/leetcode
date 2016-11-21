# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        stack = []
        if root:
            stack.append((root, root.val))
        while stack:
            node, val = stack.pop()
            if node.right:
                stack.append((node.right, node.right.val+val))
            if node.left:
                stack.append((node.left, node.left.val+val))
            if not node.right and not node.left and val == target:
                return True
        return False