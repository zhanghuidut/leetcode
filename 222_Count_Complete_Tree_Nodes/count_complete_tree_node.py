# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        rnode = root.right
        rdep = 0
        while rnode:
            rdep += 1
            rnode = rnode.right

        stack = [(root, 0)]
        num = 0
        height = -1
        while stack:
            node, dep = stack.pop()
            if dep == rdep:
                if height == -1 and not node.left and not node.right:
                    break
                elif not node.left:
                    break
                elif not node.right:
                    num += 1
                    break
                else:
                    num += 2
                    height = dep + 1
            elif dep < rdep:
                stack.append((node.right, dep+1))
                stack.append((node.left, dep+1))

        return pow(2, rdep+1)-1 + num
