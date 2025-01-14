class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_width = 0
        zeroes = 0

        #calculate number of zeroes while iterating over the array
        #keep check if number of zeroes > k; if greater check the left most element for a zero and remove that zero while increasing the window from the left side
        #calculate the width at every iteration using i-l+1 formula
        #keep track of the max width seen so far
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes+=1
            
            while zeroes > k:
                if nums[l] == 0:
                    zeroes-=1
                l+=1
            width = i-l+1
            max_width = max(max_width, width)
        return max_width