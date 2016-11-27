class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        meta, maxLen = {}, 0
        for val in nums:
            if val not in meta:
                left = meta.get(val-1, 0)
                right = meta.get(val+1, 0)
                curLen = left + right + 1
                
                maxLen = max(curLen, maxLen)
                meta[val] = curLen
                if val-left in meta:
                    meta[val-left] = curLen
                if val+right in meta:
                    meta[val+right] = curLen
        
        return maxLen
    