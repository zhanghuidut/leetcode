class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1, val in enumerate(nums):
            if target - val in nums[index1+1:]:
                return [index1, nums.index(target - val, index1+1)]
        return [-1, -1]
