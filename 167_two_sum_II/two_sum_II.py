class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)
        start = 0
        end = length -1
        while 1:
            if start >=end:
                break
            val = numbers[start] + numbers[end]
            if val == target:
                return [start + 1, end + 1]
            elif val < target:
                start += 1
            else:
                end -= 1
        return [-1, -1]
