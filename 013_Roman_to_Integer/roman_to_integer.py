class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'X': 10, 'C': 100, 'M': 1000, 'V': 5, 'L': 50, 'D':500}
        slen, index, res = len(s), 0, 0
        while index < slen:
            val = roman[s[index]]
            if index < slen-1 and roman[s[index]] < roman[s[index+1]]:
                val = roman[s[index+1]] - val
                index += 1
            else:
                while index < slen-1 and s[index] == s[index+1]:
                    val += roman[s[index]]
                    index += 1
            res += val
            index += 1
        return res
