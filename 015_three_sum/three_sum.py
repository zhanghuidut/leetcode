class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        length, res = len(nums), []
        for index in range(length-2):
            start = index + 1
            end = length -1
            while start < end:
                temp = [nums[index], nums[start], nums[end]]
                val = sum(temp)
                if val == 0:
                    if temp not in res:
                        res.append(temp)
                    start += 1
                elif val > 0:
                    end -= 1
                else:
                    start += 1
        return res
