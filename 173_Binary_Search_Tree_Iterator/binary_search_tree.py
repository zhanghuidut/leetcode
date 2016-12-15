# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.node = root
        self.stack = []

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.node or self.stack

    def next(self):
        """
        :rtype: int
        """
        while 1:
            if self.node:
                self.stack.append(self.node)
                self.node = self.node.left
            else:
                self.node = self.stack.pop()
                val = self.node.val
                self.node = self.node.right
                return val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())