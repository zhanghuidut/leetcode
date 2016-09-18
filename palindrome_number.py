class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ret = 0
        val = abs(x)
        while val:
            digit = val%10
            ret = ret*10 + digit
            val /= 10
        return (x==ret)
