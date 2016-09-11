class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length= len(nums)
        if length < 3:
            return
        result, val = sum(nums[:3]), sys.maxint
        for index1 in range(length -2):
            start, end  = index1 + 1, length -1
            while 1:
                if start >= end:
                    break
                
                s = nums[index1] + nums[start] + nums[end]
                gap = abs(s - target)

                if gap < val:
                    val = gap
                    result = s
                if s == target:
                    return target
                elif s < target:
                    start += 1
                else:
                    end -= 1
                    
        return result
                
