class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sums = []
        res, times = '', ''
        multiplicand, multiplier = (num1, num2) if len(num1) > len(num2) else (num2, num1)
        for item in multiplier[::-1]:
            val = str_multipy(multiplicand, item) + times if int(item) != 0 else '0'
            times += '0'
            sums.append(val)

        for item in sums:
            res = str_sum(res, item)
        return res

def str_multipy(mul, num):
    res, flag = '', 0
    multiplicand, multiplier = mul[::-1], int(num)
    for i in multiplicand:
        val = int(i) * multiplier
        res += str((val + flag)%10)
        flag = (val + flag)/10
    if flag:
        res += str(flag)
    return res[::-1]

def str_sum(num1, num2):
    res, flag = '', 0
    len1, len2 = len(num1), len(num2)
    str1 = num1[::-1] if num1 else ''
    str2 = num2[::-1] if num2 else ''
    for i in range(max(len1, len2)):
        val1 = str1[i] if i < len1 else 0
        val2 = str2[i] if i < len2 else 0
        val = int(val1) + int(val2) + flag
        flag = val/10
        res += str(val%10)
    if flag:
        res += str(flag)
    return res[::-1]
            
