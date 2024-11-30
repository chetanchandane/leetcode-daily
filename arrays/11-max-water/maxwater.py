def maxArea(height) -> int:
        left, right = 0, len(height) - 1
        water = 0
        while left < right:
            water = max(min(height[left], height[right]) * abs(right-left) ,  water)  
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1     
        return water          
              