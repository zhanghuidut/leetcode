class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len1, len2 = len(a), len(b)
        str1, str2 = a[::-1], b[::-1]
        flag, res = 0, ''
        for i in range(max(len1, len2)):
            val1 = int(str1[i]) if i < len1 else 0
            val2 = int(str2[i]) if i < len2 else 0
            val = val1 + val2 + flag
            flag = val/2
            res += str(val%2)
        if flag:
            res += str(flag)
        return res[::-1]
