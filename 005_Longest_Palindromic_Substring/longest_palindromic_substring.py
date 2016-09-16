# DP Time Limit Exceeded
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        maxstr = s[0]
        flag = [[0]*length for _ in range(length)]
        
        for j in range(1, length):
            for i in range(j):
                if s[i] == s[j] and (flag[i+1][j-1] or j-i<=2):
                    flag[i][j] = 1
                    maxstr = s[i:j+1] if len(maxstr)<(j+1-i) else maxstr
        return maxstr

# Accepted 
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        maxstr = s[0]
        for i in range(length):
            str1 = self.get(s, i, i)
            str2 = self.get(s, i, i+1)
            temp = str1 if len(str1) > len(str2) else str2
            maxstr = temp if len(temp) > len(maxstr) else maxstr
        return maxstr
    
    def get(self, s, i, j):
        while i>=0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]
