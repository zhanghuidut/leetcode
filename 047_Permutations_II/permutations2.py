class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(dep, path):
            if dep == h:
                ret.append(path)
            else:
                tmp = []
                for i in range(dep, h):
                    if i == dep or (nums[i] != nums[dep] and nums[i] not in tmp):
                        tmp.append(nums[i])
                        nums[dep], nums[i] = nums[i], nums[dep]
                        backtrack(dep+1, path + [nums[dep]])
                        nums[dep], nums[i] = nums[i], nums[dep]
        
        ret, h = [], len(nums)
        backtrack(0, [])
        return ret
        
