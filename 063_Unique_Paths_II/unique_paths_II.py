class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0]*n
        dp[0] = 0 if obstacleGrid[0][0] else 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j != 0:
                    dp[j] += dp[j-1]
        return dp[n-1]
        
