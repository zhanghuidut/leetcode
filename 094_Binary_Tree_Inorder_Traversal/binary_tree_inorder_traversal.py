# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        temp = root
        stack = []
        res = []
        while temp or stack:
            if temp:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                res.append(temp.val)
                temp = temp.right
        return res

# Recursive
class Solution(object):
    res = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root.left:
            self.inorderTraversal(root.left)
        self.res.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
