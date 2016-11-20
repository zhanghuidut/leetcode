# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        val = self.helper(root) if root else 1
        return True if val != -1 else False

    def helper(self, root):
        # return -1 if is not balanced else return height of subtree
        leftDep = self.helper(root.left) if root.left else 0
        rightDep = self.helper(root.right) if root.right else 0
        diff, dep = (leftDep - rightDep, leftDep+1) if leftDep > rightDep else (rightDep - leftDep, rightDep+1)
        return dep if leftDep != -1 and rightDep != -1 and diff < 2 else -1
