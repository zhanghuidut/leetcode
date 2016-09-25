class Solution(object):
    # method 1
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

    # method 2: binary search
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = [(index, val) for index, val in enumerate(nums)]
        data.sort(key=lambda x: x[1])
        start, end = 0, len(nums)-1
        while start < end:
            val = data[start][1] + data[end][1]
            if val == target:
                return [data[start][0], data[end][0]]
            elif val > target:
                end -= 1
            else:
                start += 1
        return [-1, -1]
