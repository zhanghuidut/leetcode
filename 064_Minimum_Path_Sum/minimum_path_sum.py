class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [0x7fffffff]*n
        dp[0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if j != 0:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
                elif i != 0:
                    dp[j] += grid[i][j]
        return dp[n-1]
