class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for item in strs:
            temp = sorted(item)
            temp = ''.join(temp)
            if temp in res:
                res[temp].append(item)
            else:
                res[temp] = [item]
        return res.values()
