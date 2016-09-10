class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        values = [(index, val) for index, val in enumerate(nums)]
        values.sort(key=operator.itemgetter(1))
        length = len(values)
        for index1 in range(length-2):
            start = index1 +1
            end = length -1
            while 1:
                if start == end:
                    break
                temp = [values[index1][1], values[start][1], values[end][1]]
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
