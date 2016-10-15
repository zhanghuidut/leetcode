class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = sub_sum = nums[0]
        for val in nums[1:]:
            if sub_sum < 0:
                sub_sum = val
            else:
                sub_sum += val
            
            max_sum = max(max_sum, sub_sum)
        
        return max_sum
