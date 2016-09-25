class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        romans = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["", "M", "MM", "MMM"]]
        res += romans[3][num/1000]
        num %= 1000
        res += romans[2][num/100]
        num %= 100
        res += romans[1][num/10]
        num %= 10
        res += romans[0][num]
        return res
        
