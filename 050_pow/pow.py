class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            n = 0 - n
            x = 1.0/x
        return self.myPow(x*x, n/2) if n%2 == 0 else x*self.myPow(x*x, n/2)
            
