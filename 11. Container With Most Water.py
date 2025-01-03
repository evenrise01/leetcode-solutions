#Initialize two pointers: left and right
#Find the width 
#Take the minimum of the current height between the two values at the indices and calculate the area
#Calculate the max_area found so far
#Increment/Decrement the pointers based on the current values of the indices
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while(left < right):
            width = right - left
            current_height = min(height[left],height[right])
            current_area = width*current_height

            area = max(area,current_area)

            if(height[left] < height[right]):
                left+=1
            else:
                right-=1
        return area