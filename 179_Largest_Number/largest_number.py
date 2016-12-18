class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return ''
        res = []
        for val in nums:
            res[:] = self.helper(res, str(val))
        return ''.join(res) if res[0] != '0' else '0'

    def helper(self, strs, s):
        largest = ''
        res = []
        last = None
        for i in xrange(len(strs)+1):
            if i == 0 and s == '0' and strs:
                last = strs[0]
                continue
            if last == s and i != len(strs):
                continue
            temp = list(strs)
            temp.insert(i, s)
            val = ''.join(temp)
            if val > largest:
                largest = val
                res[:] = temp
            if i < len(strs):
                last = strs[i]
        return res
