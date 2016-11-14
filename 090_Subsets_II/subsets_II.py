# backtrack
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(dep, path):
            if dep == n:
                path.sort()
                if path not in res:
                    res.append(path)
            else:
                backtrack(dep+1, path+[nums[dep]])
                backtrack(dep+1, path)
        
        res, n = [], len(nums)
        backtrack(0, [])
        return res

# iteratively
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = {()}
        for num in nums:
            res |= {r + (num,) for r in res}
        return list(res)
