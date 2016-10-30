class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rowSign, columnSign = 0, 0
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    rowSign |= (0x1<<i)
                    columnSign |= (0x1<<j)
        
        for i in range(m):
            if rowSign&0x1:
                for j in range(n):
                    matrix[i][j] = 0
            rowSign >>= 1
        
        for j in range(n):
            if columnSign&0x1:
                for i in range(m):
                    matrix[i][j] = 0
            columnSign >>= 1
