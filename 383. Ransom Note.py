class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Step 1: Create a dictionary to count the frequency of each character in magazine
        magazine_count = {}

        for char in magazine:
            magazine_count[char] = 1 + magazine_count.get(char, 0)

        # Step 2: Check if ransomNote can be constructed
        for char in ransomNote:  # Iterate through characters, not indices
            if char not in magazine_count or magazine_count[char] == 0:
                return False
            magazine_count[char] -= 1

        # If all characters in ransomNote are satisfied, return True
        return True
