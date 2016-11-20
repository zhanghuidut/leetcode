# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        val = self.helper(root) if root else (1, 1)
        return True if 'f' not in val else False

    def helper(self, root):
        if root.left:
            lminVal, lmaxVal = self.helper(root.left)
            lsign = (lmaxVal < root.val)
        else:
            lminVal, lmaxVal = root.val, root.val
            lsign = True
        
        if root.right:
            rminVal, rmaxVal = self.helper(root.right)
            rsign = (root.val < rminVal)
        else:
            rminVal, rmaxVal = root.val, root.val
            rsign = True

        if 'f' not in [lminVal, lmaxVal, rminVal, rmaxVal] and lsign and rsign:
            return lminVal, rmaxVal
        else:
            return ('f', 'f')
