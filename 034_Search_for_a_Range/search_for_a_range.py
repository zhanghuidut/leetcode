class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end)/2
            if nums[mid] == target:
                first = self.getstart(nums, start, mid, target)
                second = self.getend(nums, mid, end, target)
                return [first, second]
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return [-1, -1]
        
    def getstart(self, nums, start, end, target):
        while start <= end:
            mid = (start + end)/2
            if nums[mid] == target:
                if mid==start or nums[mid-1] < target:
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid + 1

    
    def getend(self, nums, start, end, target):
        while start <= end:
            mid = (start + end)/2
            if nums[mid] == target:
                if mid == end or nums[mid+1] > target:
                    return mid
                else:
                    start = mid + 1
            else:
                end = mid -1

