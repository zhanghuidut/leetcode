class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(dep, path):
            if dep == n:
                if len(path) == k:
                    res.append(path)
            else:
                backtrack(dep+1, path+[dep+1])
                backtrack(dep+1, path)
        
        res = []
        backtrack(0, [])
        return res
