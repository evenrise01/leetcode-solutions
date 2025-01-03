class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        maxLeft, maxRight = height[l],height[r]

        while l < r:
            if maxLeft < maxRight:
                l+=1 #Move left pointer
                maxLeft = max(maxLeft,height[l])
                res+=maxLeft - height[l]
            else:
                r-=1 #Move right pointer
                maxRight = max(maxRight, height[r])
                res+= maxRight - height[r]
        return res