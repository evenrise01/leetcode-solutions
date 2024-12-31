class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n] = i
#Time complexity O(n)
#Space complexity O(n)
#Take the difference of target - current index, store in hashmap, check if difference is in hashmap, return the indices
            