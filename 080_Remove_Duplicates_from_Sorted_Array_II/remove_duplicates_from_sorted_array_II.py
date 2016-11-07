class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k, n = -1, 1
        for i in xrange(len(nums)):
            if k == -1 or nums[k] != nums[i]:
                k += 1
                n = 1
                nums[k] = nums[i]
            elif n < 2 and nums[k] == nums[i]:
                k += 1
                n += 1
                nums[k] = nums[i]

        return k+1
