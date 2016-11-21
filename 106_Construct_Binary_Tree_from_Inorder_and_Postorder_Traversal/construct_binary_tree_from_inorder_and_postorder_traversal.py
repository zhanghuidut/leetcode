# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder and postorder:
            return self.helper(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)
    
    def helper(self, inorder, postorder, inorderStart, inorderEnd, postorderStart, postorderEnd):
        if inorderStart <= inorderEnd and postorderStart <= postorderEnd:
            val = postorder[postorderEnd]
            pos = inorder.index(val)
            root = TreeNode(val)

            root.left = self.helper(inorder, postorder, inorderStart, pos-1, postorderStart, postorderStart+pos-inorderStart-1)
            root.right = self.helper(inorder, postorder, pos+1, inorderEnd, postorderStart+pos-inorderStart, postorderEnd-1)
            return root
