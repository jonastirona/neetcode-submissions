class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0

        for left in range(len(heights) - 1):
            right = len(heights) - 1
            while left < right:
                current = min(heights[left], heights[right])*(right - left)
                maximum = max(current, maximum)
                right-=1

        return maximum