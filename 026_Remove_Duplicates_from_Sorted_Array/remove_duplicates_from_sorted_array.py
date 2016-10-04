class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index, val = -1, None
        for integer in nums:
            if integer != val:
                index += 1
                val = integer
                nums[index] = integer
        return index+1
