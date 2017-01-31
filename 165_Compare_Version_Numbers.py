
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        len1, len2 = len(v1), len(v2)
        num = max(len1, len2)
        for i in xrange(num):
            n1 = 0 if i >= len1 else int(v1[i])
            n2 = 0 if i >= len2 else int(v2[i])

            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        return 0

