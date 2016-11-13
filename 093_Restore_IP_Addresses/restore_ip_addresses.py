class Solution(object):
    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtrack(dep, path, pos):
            if dep == 3:
                temp, n = s[pos:], len(s[pos:])
                if temp and n in ranges and int(temp) in ranges[n]:
                    res.append(path+temp)
            else:
                for i in range(1, 4):
                    temp = s[pos:(pos+i)]
                    if temp and int(temp) in ranges[i]:
                        backtrack(dep+1, path+temp+'.', pos+i)
        res = []
        ranges = {1: xrange(10), 2: xrange(10, 100), 3: xrange(100, 256)}
        backtrack(0, '', 0)
        return res
