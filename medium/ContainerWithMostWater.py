from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        best_square = 0
        while l < r:
            local_square = min(height[l], height[r])*(r-l)
            best_square = max(best_square, local_square)
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
        return best_square