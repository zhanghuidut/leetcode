# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxDep, stack = 0, []
        if root:
            stack.append((root, 1))
        while stack:
            node, dep = stack.pop()
            if node.left:
                stack.append((node.left, dep+1))
            if node.right:
                stack.append((node.right, dep+1))
            if not node.left and not node.right:
                maxDep = max(dep, maxDep)
        return maxDep