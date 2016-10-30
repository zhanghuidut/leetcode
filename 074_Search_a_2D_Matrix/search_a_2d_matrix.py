class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        start, end = 0, (m-1)*n + n-1
        while start <= end:
            mid = start + (end - start)/2
            mrow, mcol = mid/n, mid%n
            if matrix[mrow][mcol] == target:
                return True
            elif matrix[mrow][mcol] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
