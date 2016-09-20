class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len1, len2 = len(s), len(p)
        p1, p2 = 0, 0
        last = ''
        while (p1 < len1) and (p2 < len2):
            cur = p1
            if p[p2] == '.' or p[p2] ==s[p1]:
                p2 += 1
                p1 += 1
            elif p[p2] == '*':
                while s[p1] == s[last]:
                    p1 += 1
                p2 + =1
            elif p[p2] !=s[p1]:
                return False
            
            last = s[cur]

        if p1==len1 - 1 and p2==len2 - 1:
            return True
        else:
            return False
