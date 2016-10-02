class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in mapping:
                try:
                    tmp = stack.pop() 
                except IndexError:
                    return False
                else:
                    if tmp != mapping[ch]:
                        return False
            else:
                stack.append(ch)

        return False if stack else True
            
            
