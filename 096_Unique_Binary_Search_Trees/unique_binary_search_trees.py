class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [[0]*n for _ in range(n)]
        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                if i >= j:
                    res[i][j] = 1
                else:
                    for k in range(i, j+1):
                        lval = res[i][k-1] if k != i else 1
                        rval = res[k+1][j] if k != j else 1
                        res[i][j] += (lval*rval)
        return res[0][n-1]
        
