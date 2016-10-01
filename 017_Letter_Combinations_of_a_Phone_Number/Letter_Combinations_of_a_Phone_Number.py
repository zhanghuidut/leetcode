# 迭代回朔
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        d, h = 0, len(digits)-1
        index, tmp, res = [-1]*(h+1), '', []
        while d > -1:
            index[d] += 1
            strs = mapping[digits[d]]
            if index[d] < len(strs):
                tmp += strs[index[d]]
                if d == h:
                    res.append(tmp)
                    tmp = tmp[:-1]
                else:
                    d += 1
                    index[d] = -1
            else:
                d -= 1
                tmp = tmp[:-1]

        return res
            
            
