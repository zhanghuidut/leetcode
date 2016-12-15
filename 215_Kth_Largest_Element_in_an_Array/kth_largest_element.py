class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = len(nums)
        return self.helper(nums, 0, m-1, m-k)
    
    def helper(self, nums, start, end, k):
        val = nums[end]
        i = start-1
        for j in xrange(start, end):
            if nums[j] < val:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[i], nums[end] = nums[end], nums[i]
        n = i-start
        if n == k:
            return nums[i]
        elif n < k:
            return self.helper(nums, i+1, end, k-n-1)
        else:
            return self.helper(nums, start, i-1, k)

