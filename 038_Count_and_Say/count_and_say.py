class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i, ret = 1, '1'
        while i < n:
            cout, val, temp = 0, '', ''
            for ch in ret:
                if ch != val:
                    if cout != 0:
                        temp += (str(cout) + val)
                    cout, val = 1, ch
                else:
                    cout += 1
            temp += (str(cout) + val)
            ret = temp
            i += 1
        return ret
