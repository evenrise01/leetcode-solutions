# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float(-inf)
        current_sum = 0

        for i in range(0,len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum