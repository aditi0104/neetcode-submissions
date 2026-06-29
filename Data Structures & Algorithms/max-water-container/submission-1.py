class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, h = 0, len(heights) - 1
        maxArea = 0
        while l < h:
            area = (h - l)*min((heights[h], heights[l]))
            maxArea = max(maxArea, area)
            if heights[l] < heights[h]:
                l = l + 1
            else:
                h = h - 1
        return maxArea
        