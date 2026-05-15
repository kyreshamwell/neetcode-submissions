class Solution:
    def maxArea(self, heights: List[int]) -> int:

        arr = []

        left = 0 
        right = len(heights) -1 

        while left < right:

            width = right - left
            height = min(heights[left], heights[right])
            water = width * height
            arr.append(water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max(arr)
        