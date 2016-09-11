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
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        test = [(index, val) for index, val in enumerate(nums)]
        test.sort(cmp=lambda x, y: cmp(x[1], y[1]))
        
        start = 0
        end = len(test) -1
        while 1:
            if start == end:
                break
            val = test[start][1] + test[end][1]
            if val == target:
                return [test[start][0], test[end][0]]
            elif val < target:
                start += 1
            else:
                end -= 1
        return [-1, -1]
