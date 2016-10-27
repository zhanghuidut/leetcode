# backtrack  Time limit exceeded
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def backtrack(i, j):
            if i == m-1 and j == n-1:
                self.res += 1
            else:
                if i+1 < m:
                    backtrack(i+1, j)
                if j+1 < n:
                    backtrack(i, j+1)

        self.res = 0
        backtrack(0, 0)
        return self.res

# AC
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = factorial(m+n-2)/(factorial(m-1)*factorial(n-1))
        return res
    
def factorial(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res
