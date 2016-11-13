class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.makeTree(1, n)

    def makeTree(self, i, j):
        temp = []
        if i <= j:
            for k in range(i, j+1):
                lsubTree = self.makeTree(i, k-1)
                rsubTree = self.makeTree(k+1, j)
                for left in lsubTree:
                    for right in rsubTree:
                        root = TreeNode(k)
                        root.left = left
                        root.right = right
                        temp.append(root)
        else:
            temp.append(None)
        return temp
