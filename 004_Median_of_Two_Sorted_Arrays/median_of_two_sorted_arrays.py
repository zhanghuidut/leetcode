# 二分搜索 O(lgn)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        if length&0x1 == 1:
            return self.findKth(nums1, nums2, length/2+1)
        else:
            n1 = self.findKth(nums1, nums2, length/2+1)
            n2 = self.findKth(nums1, nums2, length/2)
            return (n1 + n2)/2.0

    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findKth(nums2, nums1, k)
        if not nums1:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        in1 = min(len(nums1), k/2)
        in2 = k - in1
        if nums1[in1-1] == nums2[in2-1]:
            return nums1[in1-1]
        elif nums1[in1-1] < nums2[in2-1]:
            return self.findKth(nums1[in1:], nums2, k-in1)
        else:
            return self.findKth(nums1, nums2[in2:], k-in2)

# 二路归并 O(n)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = self.merge(nums1, nums2)
        length = len(nums)
        if length%2 == 0:
            return (nums[length/2] + nums[length/2 -1])/2.0
        else:
            return nums[length/2]
        
    def merge(self, nums1, nums2):
        nums, length = [], len(nums1) + len(nums2)
        index1, index2 = 0, 0
        nums1.append(sys.maxint)
        nums2.append(sys.maxint)
        for i in range(length):
            if nums1[index1] < nums2[index2]:
                nums.append(nums1[index1])
                index1 += 1
            else:
                nums.append(nums2[index2])
                index2 += 1
        return nums
