class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        length, values, result = len(nums), {}, set()
        for i in range(2, length-1):
            for j in range(i+1, length):
                temp = [nums[i], nums[j]]
                if sum(temp) not in values:
                    values[sum(temp)] = [(i, j)]
                else:
                    values[sum(temp)].append((i, j))

        for i in range(length-3):
            for j in range(i+1, length-2):
                val = target -nums[i] - nums[j]
                for temp in values.get(val, []):
                    
                    if temp[0] > j:
                        result.add((nums[i], nums[j], nums[temp[0]], nums[temp[1]]))

        return [list(item) for item in result]
