class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Note: While we can use stack approach to push half of the string and pop the other half to verify
        #       this approach would take O(N) time and O(N) space
        #
        #       The better approach is to use two pointers, so while time space is O(N)
        #       the space complexity is O(1)

        left = 0
        right = len(s) - 1
        
        while left < right:
            # Move left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare characters at the left and right pointers
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers toward middle of string
            left += 1
            right -= 1
        
        return True