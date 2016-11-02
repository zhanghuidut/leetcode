class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        c = [0]*3
        for i in nums:
            c[i] += 1
        
        for i in range(1, 3):
            c[i] += c[i-1]
        
        start = 0
        for index, val in enumerate(c):
            if start != val:
                nums[start:val] = [index]*(val-start)
                start = val
