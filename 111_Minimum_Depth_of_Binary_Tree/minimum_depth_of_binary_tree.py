# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = []
        minDep = 0x7ffffff
        stack.append((root, 1))
        while stack:
            node, dep = stack.pop()
            if dep < minDep:
                if node.right:
                    stack.append((node.right, dep+1))
                if node.left:
                    stack.append((node.left, dep+1))
                if (not node.left) and (not node.right):
                    minDep = min(minDep, dep)
        return minDep
