class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        m, n = len(matrix)-1, len(matrix[0])-1
        i = 0
        res = []
        while i <= n and i <= m:
            k, l = 0, 1
            temp1, temp2, temp3, temp4 = [], [], [], []
            while i + k <= n:
                temp1.append(matrix[i][i+k])
                if i != m:
                    temp3.append(matrix[m][n-k])
                k += 1

            while i + l < m:
                temp2.append(matrix[i+l][n])
                if i != n:
                    temp4.append(matrix[m-l][i])
                l += 1
            i += 1
            m -= 1
            n -= 1
            res += temp1 + temp2 + temp3 + temp4
            
        return res
