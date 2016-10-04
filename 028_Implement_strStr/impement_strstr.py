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
