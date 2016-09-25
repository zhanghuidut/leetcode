class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxA = 0
        start, end = 0, len(height) - 1
        while start < end:
            maxA = max(maxA, min(height[start], height[end])*(end-start))
            if height[start] > height[end]:
                if height[end] < height[end-1]:
                    end -= 1
                else:
                    while end > start and height[end] >= height[end-1]:
                        end -= 1
            else:
                if height[start] < height[start+1]:
                    start += 1
                else:
                    while end > start and height[start] >= height[start+1]:
                        start += 1
        return maxA
