class Solution:
    def trap(self, height):  
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        while (left < right):
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if (left_max < right_max): 
                res += left_max - height[left]
                left += 1
            else: 
                res += right_max - height[right]
                right -= 1
        
        return res