class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        temp = root
        while temp or stack:
            if temp:
                res.append(temp.val)
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                temp = temp.right
        return res
