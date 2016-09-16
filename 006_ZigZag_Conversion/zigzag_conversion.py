class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = ['' for _ in range(numRows)]
        n, acc = 0, 1
        for i in s:
            if n == 0:
                acc = 1
            elif n == (numRows -1):
                acc = -1

            res[n] += i
            n += acc
            
        return ''.join(res)
