class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = -1
        for integer in nums:
            if integer != val:
                index += 1
                nums[index] = integer
        
        return index+1
