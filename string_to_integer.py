class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX, INT_MIN = 0x7fffffff, -1-0x7fffffff
        ind, ret, sign, length = 0, 0, 1, len(str)
        for i, ch in enumerate(str):
            if ch != ' ':
                ind = i
                break

        if ind < length and str[ind] in ['-', '+']:
            sign = -1 if str[ind] == '-' else 1
            ind += 1

        while ind < length and str[ind].isdigit():
            digit = int(str[ind])
            MAX_VAL = INT_MAX if sign == 1 else (0 - INT_MIN)
            overflow = False if ret == 0 or (MAX_VAL - digit)/(ret*1.0) >=10 else True
            if overflow:
                return (INT_MAX if sign==1 else INT_MIN)
            else:
                ret = ret*10 + int(str[ind])
            ind += 1
        return sign*ret
