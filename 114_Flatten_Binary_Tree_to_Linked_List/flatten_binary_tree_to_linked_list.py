# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        first = last = None
        temp = root
        res, stack = [], []
        while temp or stack:
            if temp:
                res.append(temp)
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                temp = temp.right
        for node in res:
            node.left = None
            if first:
                last.right = node
                last = node
            else:
                first = last = node

