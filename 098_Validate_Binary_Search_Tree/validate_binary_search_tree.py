# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        left = root.val > self.getMaxValue(root.left) and self.isValidBST(root.left) if root.left else True

        if not left:
            return False
        
        return root.val < self.getMinValue(root.right) and self.isValidBST(root.right) if root.right else True


    def getMaxValue(self, root):
        while root.right:
            root = root.right
        return root.val

    def getMinValue(self, root):
        while root.left:
            root = root.left
        return root.val
