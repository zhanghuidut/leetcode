# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        temp = root
        stack, res = [], []
        while temp or stack:
            if temp:
                stack.append([temp, 'left'])
                temp = temp.left
            else:
                node, tag = stack[-1]
                if tag == 'left':
                    stack[-1][1] = 'right'
                    temp = node.right
                else:
                    stack.pop()
                    res.append(node.val)
                    temp = None
        return res
