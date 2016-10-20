# DFS Time limit  exceeded
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return Ture

        stack = [0]
        lens = len(nums)
        while stack:
            index = stack.pop()
            if index == lens-1:
                return True
            elif index > lens-1:
                continue

            steps = [index+i for i in range(1, nums[index]+1)]
            stack += steps
        return False
        
 
 # AC
 class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        pos = n
        for i in xrange(n-1, -1, -1):
            if i + nums[i] >= n -1 or i + nums[i] >= pos:
                pos = i
        return pos == 0
