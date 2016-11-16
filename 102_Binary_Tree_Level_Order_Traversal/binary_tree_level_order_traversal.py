# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack, res, temp = [], [], []
        if root:
            stack.append(root)
            stack.append(TreeNode(None))
        while stack:
            node = stack.pop(0)
            if node.val is not None:
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            elif temp:
                stack.append(node)
                res.append(temp)
                temp = []
        return res
