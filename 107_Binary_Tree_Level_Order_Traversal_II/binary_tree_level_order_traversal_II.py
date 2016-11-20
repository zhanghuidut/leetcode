# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, queue, temp = [], [], []
        if root:
            queue.extend([root, TreeNode(None)])
        while queue:
            node = queue.pop(0)
            if node.val is not None:
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            elif temp:
                res.insert(0, temp)
                temp = []
                queue.append(node)
        return res