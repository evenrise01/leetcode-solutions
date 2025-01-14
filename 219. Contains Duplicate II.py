class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Use a set to store the elements in the current window
        window = set()
        
        for end in range(len(nums)):
            # If the current number is already in the set, a duplicate is found
            if nums[end] in window:
                return True
            
            # Add the current number to the set
            window.add(nums[end])
            
            # Maintain the size of the sliding window to at most k
            if len(window) > k:
                window.remove(nums[end - k])  # Remove the leftmost element
        
        # If no duplicates are found
        return False