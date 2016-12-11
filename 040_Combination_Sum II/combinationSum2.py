class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        subset = [[]]
        res = []
        candidates.sort()
        last = 0
        for i in xrange(len(candidates)):
            temp = []
            for j in xrange(len(subset)):
                if sum(subset[j]) < target and:
                    if i > 0 and candidates[i] == candidates[i-1] and j < last:
                        continue
                    t = subset[j]+[candidates[i]]
                    temp.append(t)
                    if sum(t) == target:
                        res.append(t)
            last = len(subset)
            subset += temp
        return res

# debug
candidates = [10,1,2,7,6,1,5]
target = 8
print Solution().combinationSum2(candidates, target)
    