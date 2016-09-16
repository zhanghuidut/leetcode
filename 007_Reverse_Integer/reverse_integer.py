class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = pow(2, 31)
        sign = -1 if x<0 else 1
        str_x = str(abs(x))
        str_int = int(str_x[::-1])
        cond = str_int <= MAX_INT if sign == -1 else str_int < MAX_INT
        int_x = str_int if cond else 0

        return sign*int_x

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX_VAL = pow(2, 31)
        sign = -1 if x<0 else 1
        val, ret = abs(x), 0
        while val:
            digit = val%10
            temp = (INT_MAX_VAL-digit)/(ret*1.0) if ret != 0 else 100
            cond = (temp > 10) if sign == 1 else (temp >= 10)

            if cond:
                ret = ret*10 + digit
            else:
                return 0
                
            val /= 10
        return sign*ret
