class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # O(n) time complexity - iterating through length n of string
        # O(1) space complexity - using variable i in single pass

        length = 0
        i = len(s) - 1
        
        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Count the length of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length