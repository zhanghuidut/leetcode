# Time Limit Exceeded 
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        slen, plen = len(s), len(p)
        if slen == 0 and plen == 0:
            return True
        elif plen == 0:
            return False
        
        if plen > 1 and p[1] == '*':
            index = 0
            while index < slen and (s[index] == p[0] or p[0] == '.'):
                if self.isMatch(s[index+1:], p[2:]):
                    return True
                index += 1
            if self.isMatch(s, p[2:]):
                return True
        elif slen > 0:
            if s[0] == p[0] or p[0] == '.':
                return self.isMatch(s[1:], p[1:])

        return False
    

            
