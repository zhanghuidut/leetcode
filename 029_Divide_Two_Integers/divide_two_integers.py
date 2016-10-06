class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or (dividend==-2147483648 and divisor==-1):
            return 0x7fffffff
        
        sign = -1 if (dividend<0)^(divisor<0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        rem, ret = dividend, 0
        while rem>=divisor:
            i, temp = 0, divisor<<1
            while rem>temp:
                i += 1
                temp = temp<<1

            ret += (1<<i)
            rem -= (divisor<<i)
        return sign*ret

#note:
#python中数字类型的范围大于int，若用c则需考虑dividend, divisor取绝对值时转换为long int,temp也应为long int，否则会溢出出错
#python负数/数字对应的二进制究竟是怎样的？需要研究下
