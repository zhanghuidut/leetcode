# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, temp, stack1, stack2 = [], [], [], []
        if root:
            stack1.append(root)
        while stack1 or stack2:
            while stack1:
                node = stack1.pop()
                temp.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            if temp:
                res.append(temp)
                temp = []
            while stack2:
                node = stack2.pop()
                temp.append(node.val)
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)

            if temp:
                res.append(temp)
                temp = []
        return res
