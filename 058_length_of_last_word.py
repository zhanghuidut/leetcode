class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastlen, curlen = 0, 0
        for ch in s:
            if ch == ' ':
                if curlen != 0:
                    lastlen = curlen
                curlen = 0
            else:
                curlen += 1
        if curlen != 0:
            lastlen = curlen
        return lastlen
