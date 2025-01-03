class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        while(left < right):
            current_sum = numbers[left] + numbers[right]

            if(current_sum == target):
                return left + 1, right + 1
            if(current_sum < target):
                left+=1
            else:
                right-=1
        return {}
    

#Two pointers - initialize left at start, right at end. Check for the sum at the left and right, if target found return left + 1, right + 1 (Because it is 1-indexed), if target not equal current sum, move the pointers based on if the current is larger or less than the target. [Sorted array makes it easier]