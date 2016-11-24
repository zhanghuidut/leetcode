class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxVal, minVal = 0, 0
        for ind, val in enumerate(prices):
            if ind == 0:
                minVal = val
            else:
                maxVal = max(val-minVal, maxVal)
                minVal = min(minVal, val)
        return maxVal
