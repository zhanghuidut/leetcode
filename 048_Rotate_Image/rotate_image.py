class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        i, j = 0, len(matrix[0])-1
        while i < j:
            k = 0
            while k < j-i:
                matrix[i][i+k], matrix[i+k][j], matrix[j][j-k], matrix[j-k][i] = \
                matrix[j-k][i], matrix[i][i+k], matrix[i+k][j], matrix[j][j-k]
                k += 1
            i += 1
            j -= 1
            
