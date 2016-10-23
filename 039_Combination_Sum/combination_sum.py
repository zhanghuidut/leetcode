# 递归
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(dep, path):
            if dep < n:
                for i in range(nums[dep][0]+1):
                    temp = path + [nums[dep][1]]*i
                    sums = sum(temp)
                    if sums == target:
                        res.append(temp)
                    elif sums < target:
                        backtrack(dep + 1, temp)
        
        n, res = len(candidates), []
        nums = [(target/item, item) for item in candidates]
        backtrack(0, [])
        return res
 
# 迭代
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n, res = len(candidates), []
        nums = [(target/item, item) for item in candidates]
        
        dep = 0
        index = [-1]*n
        path = []
        while dep > -1:
            index[dep] += 1
            if index[dep] <= nums[dep][0]:
                temp = path + [nums[dep][1]]*index[dep]
                if sum(temp) == target:
                    res.append(temp)
                elif sum(temp) < target:
                    if dep < n-1:
                        dep += 1
                        index[dep] = -1
                        path = temp
                else:
                    dep -= 1
                    if index[dep] != 0:
                        path = path[:(-index[dep])]
            else:
                dep -= 1
                if index[dep] != 0:
                    path = path[:(-index[dep])]

        return res

