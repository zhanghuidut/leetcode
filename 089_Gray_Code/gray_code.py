class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for val in range(pow(2, n)):
            offset = val >> 1
            val ^= offset
            res.append(val)
        return res
