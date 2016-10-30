class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        dp = [0]*(n+1)
        for i in range(n+1):
            if i >=2:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = i+1
        
        return dp[n-1]
        
