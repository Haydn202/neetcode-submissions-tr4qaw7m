class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxWater = 0

        while right < len(heights) and left < right:
            height = min(heights[left], heights[right])
            width = right - left
            water = height * width

            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1 

            if water > maxWater:
                maxWater = water
                    
        return maxWater
            
