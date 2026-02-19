class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWaterArea = 0
        left = 0
        right = len(height)-1
        while left<right:
            h = right - left
            b = min(height[left], height[right])
            curr_area = h * b
            maxWaterArea = max(maxWaterArea, curr_area)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return maxWaterArea