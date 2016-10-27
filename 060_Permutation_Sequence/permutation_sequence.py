class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i+1) for i in range(n)]
        k %= factorial(n)
        res = []
        i = 0
        while 1:
            val = factorial(n-i-1)
            quo, rem = (k-1)/val, k%val
            res.append(nums[quo])
            del nums[quo]
            if rem == 0:
                nums.sort(reverse=True)
                res += nums
                return ''.join(res)
            else:
                k = rem
                i += 1
    
def factorial(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res
