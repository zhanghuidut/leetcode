class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix, index = '', 0
        while 1:
            try:
                ch = strs[0][index]
            except IndexError:
                return prefix

            for item in strs:
                try:
                    val = item[index]
                except IndexError:
                    return prefix
                if val != ch:
                    return prefix

            prefix += ch
            index += 1
        return prefix


