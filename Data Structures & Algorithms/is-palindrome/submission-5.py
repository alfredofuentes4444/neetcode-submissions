class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = s.replace(" ", "").lower().replace("?", "").replace(",", "").replace("'", "").replace(".", "").replace(":", "").replace("!", "")
        
        left = 0
        right = len(new_string) - 1

        while left < right:
            for i in range(len(new_string)):
                if new_string[left] != new_string[right]:
                    return False
                left += 1
                right -= 1
        
        return True
