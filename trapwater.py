class Solution:
    def trap(self, height):
        stack = []
        water = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                mid = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(h, height[stack[-1]]) - height[mid]
                water += distance * bounded_height
            stack.append(i)
        return water


s = Solution()
print(s.trap([4,2,0,3,2,5]))  
