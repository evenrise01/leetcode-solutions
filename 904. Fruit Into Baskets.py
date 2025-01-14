class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Dictionary to store the count of each fruit type in the current window
        fruit_count = {}
        max_fruits = 0  # To track the maximum number of fruits we can collect
        start = 0  # Left pointer of the sliding window
        
        for end in range(len(fruits)):
            # Add the current fruit to the dictionary and increment its count
            fruit = fruits[end]
            fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
            
            # If we have more than 2 distinct fruits, shrink the window
            while len(fruit_count) > 2:
                fruit_to_remove = fruits[start]
                fruit_count[fruit_to_remove] -= 1
                if fruit_count[fruit_to_remove] == 0:
                    del fruit_count[fruit_to_remove]  # Remove the fruit from the dictionary
                start += 1  # Shrink the window by moving the left pointer
            
            # Update the maximum number of fruits collected
            max_fruits = max(max_fruits, end - start + 1)
        
        return max_fruits