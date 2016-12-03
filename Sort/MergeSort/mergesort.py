class Solution(object):
    self.reversenums = 0 #逆序对
    def merge_sort(self, nums, start, end):
        if start < end:
            mid = (start + end)/2
            self.merge_sort(nums, start, mid)
            self.merge_sort(nums, mid+1, end)
            self.merge(nums, start, mid, end)
   
    def merge(self, nums, start, mid, end):
        temp = []
        i, j = start, mid+1
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                self.reversenums += (mid-i+1) #逆序对
                temp.append(nums[j])
                j += 1
        
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= end:
            temp.append(nums[j])
            j += 1
        nums[start:(end+1)] = temp
