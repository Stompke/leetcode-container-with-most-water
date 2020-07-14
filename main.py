
def check_vol(h_left, h_right, width):
    return min(h_left, h_right) * width
    

class Solution:
    def firstPass(self, height: List[int]) -> int:
        max_vol = 0
        for left in range(len(height)):
            for right in range(left+1,len(height)):
                vol = check_vol(height[left], height[right], right - left)
                max_vol = max(max_vol, vol)
                print(f"{left} and {right} volume is {vol}")
        return max_vol
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_vol = 0
        while left < right:
            vol = check_vol(height[left], height[right], right - left)
            if height[left] < height[right]:
                left = left+1
            else:
                right = right -1
            max_vol = max(max_vol, vol)
        return max_vol
                
        