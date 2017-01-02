# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, queue = [], []
        if root:
            queue[:] = [root, None]
        while queue:
            node1 = queue.pop(0)
            node2 = queue[0]
            if node1.left:
                queue.append(node1.left)
            if node1.right:
                queue.append(node1.right)
            if node2 is None:
                queue.pop(0)
                if queue:
                    queue.append(None)
                res.append(node1.val)
        return res

