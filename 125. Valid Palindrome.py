class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = ''.join(filter(str.isalnum, s)).lower()
        left = 0
        right = len(cleaned_text) - 1

        while (left < right):
            if(cleaned_text[left] != cleaned_text[right]):
                return False
            left+=1
            right-=1

        return True