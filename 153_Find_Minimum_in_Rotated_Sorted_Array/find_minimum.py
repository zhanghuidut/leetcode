class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        start, end = 0, len(nums)
        temp = nums[0]
        if nums[start] > nums[end-1]:
            while start < end:
                mid = (start + end)/2
                if nums[start] > nums[start+1]:
                    return nums[start+1]
                elif nums[start] < nums[mid]:
                    start = mid
                else:
                    end = mid
        else:
            return nums[start]
