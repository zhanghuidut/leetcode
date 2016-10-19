class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sign = 1
        for i in range(len(digits)-1, -1, -1):
            val = digits[i] + sign
            sign = 1 if val >= 10 else 0
            digits[i] = val%10
        if sign:
            digits.insert(0, 1)
        return digits
            
