# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder and inorder:
            return self.build(preorder, inorder, 0, len(preorder), 0, len(inorder))

    def build(self, preorder, inorder, preorderStart, preorderEnd, inorderStart, inorderEnd):
        if preorderStart < preorderEnd and inorderStart < inorderEnd:
            val = preorder[preorderStart]
            pos = inorder.index(val)
            root = TreeNode(val)
            
            root.left = self.build(preorder, inorder, preorderStart+1, preorderStart+pos+1-inorderStart, inorderStart, pos)
            root.right = self.build(preorder, inorder, preorderStart+pos+1-inorderStart, preorderEnd, pos+1, inorderEnd)
            return root


