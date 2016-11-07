class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        k, n = 0, 1
        for i in xrange(1, len(nums)):
            if n < 2 and nums[k] == nums[i]:
                k += 1
                n += 1
                nums[k] = nums[i]
            elif nums[k] != nums[i]:
                k += 1
                n = 1
                nums[k] = nums[i]

        return k+1
