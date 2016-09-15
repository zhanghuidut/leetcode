class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashtable = {ch: -1 for ch in s}
        maxlen, start = 0, 0
        for index, ch in enumerate(s):
            if hashtable[ch] != -1:
                start = hashtable[ch] + 1
                for key, value in hashtable.items():
                    if value < hashtable[ch]:
                        hashtable[key] = -1
                hashtable[ch] = index
            else:
                hashtable[ch] = index
                maxlen = max(index - start + 1, maxlen)
        return maxlen
