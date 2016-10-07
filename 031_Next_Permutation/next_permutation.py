class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)
        for i in range(nlen-2, -1, -1):
            j = self.getlarger(i, nums)
            if j:
                nums[j], nums[i] = nums[i], nums[j]
                self.quicksort(nums, i+1, nlen-1)
                return
        self.quicksort(nums, 0, nlen-1)

    def getlarger(self, index, nums):
        val, nlen = nums[index], len(nums)
        for i in range(index+1, nlen):
            if (i == nlen -1 and nums[i] > val) or (nums[i] > val and nums[i+1]<=val):
                return i

    def quicksort(self, nums, start, end):
        if start < end:
            q = self.partition(nums, start, end)
            self.quicksort(nums, start, q-1)
            self.quicksort(nums, q+1, end)

    def partition(self, nums, start, end):
        x = nums[end]
        i = start-1
        for j in range(start, end):
            if nums[j] < x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        nums[i+1], nums[end] = nums[end], nums[i+1]
        return i+1

#note:
#相关题目：《算导》p24逆序对
