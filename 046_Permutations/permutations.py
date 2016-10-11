class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(dep, path):
            if dep == h:
                ret.append(path)
            else:
                for i in range(dep, h):
                    nums[dep], nums[i] = nums[i], nums[dep]
                    backtrack(dep+1, path + [nums[dep]])
                    nums[dep], nums[i] = nums[i], nums[dep]
        
        ret, h = [], len(nums)
        backtrack(0, [])
        return ret
        
