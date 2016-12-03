# python
import math
def radixsort(nums):
    """
    :type root: TreeNode
    :rtype: int
    """
    b = getMaxBit(nums)
    for i in range(b):
        buf = {i: [] for i in range(10)}
        for num in nums:
            n = getBit(num, i)
            buf[n].append(num)
        nums = [j for i in buf.values() for j in i]
    return nums

def getMaxBit(nums):
    if not nums:
        return 0
    maxBit = 1
    for val in nums:
        
        while math.floor(val/math.pow(10, maxBit)):
            maxBit += 1
    return maxBit

def getBit(num, n):
    for i in range(n):
        num /= 10
    return num%10

nums = [278, 109, 63, 930, 589, 184, 505, 269, 8, 83]
print radixsort(nums)
