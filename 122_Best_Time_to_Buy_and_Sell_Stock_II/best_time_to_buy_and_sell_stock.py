# DP TLE
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        f = [[0]*n for _ in range(n)]
        for i in xrange(n-1, -1, -1):
            for j in xrange(i+1, n):
                val = prices[j] -prices[i]
                for k in range(i, j):
                    val = max(f[i][k]+f[k+1][j], val)
                f[i][j] = val

        return f[0][n-1]

# GREEDY  AC
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res, n = 0, len(prices)
        for i in range(n-1):
            if prices[i+1]>prices[i]:
                res += (prices[i+1] - prices[i])

        return res
