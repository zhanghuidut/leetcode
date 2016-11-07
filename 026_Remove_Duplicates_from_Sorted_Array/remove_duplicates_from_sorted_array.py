class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = -1
        for i in xrange(len(nums)):
            if k == -1 or nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k+1
