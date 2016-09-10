class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        length = len(nums)
        for index1 in range(length-2):
            start = index1 +1
            end = length -1
            while 1:
                if start == end:
                    break
                temp = [nums[index1], nums[start], nums[end]]
                val = sum(temp)
                if val == 0:
                    if temp not in result:
                        result.append(temp)
                    start += 1
                elif val < 0:
                    start += 1
                else:
                    end -= 1

        return result
