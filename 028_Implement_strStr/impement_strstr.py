# BF O(mn)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len1, len2 = len(haystack), len(needle)
        i, j = 0, 0
        while 1:
            if j == len2:
                return i-len2
            if i == len1:
                return -1

            if haystack[i] == needle[j]:
                j += 1
                i += 1
            else:
                i = i - j + 1
                j = 0
#KMP O(m+n)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len1, len2 = len(haystack), len(needle)
        i, j = 0, 0
        nexts = self.getnext(needle)
        while 1:
            if j == len2:
                return i - len2
            if i == len1:
                return -1
            if haystack[i] == needle[j]:
                j += 1
                i += 1
            elif j == 0:
                i += 1
            else:
                j = nexts[j-1]
    
    def getnext(self, needle):
        nums = len(needle)
        nexts = [0]*nums
        i = 1
        j = 0
        while i < nums:
            if needle[i] == needle[j]:
                nexts[i] = j + 1
                i += 1
                j += 1
            elif j == 0:
                nexts[i] = 0
                i += 1
            else:
                j = nexts[j-1]
        return nexts
