class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Strategy: Sliding Window + Two Pointers
        # Time Complexity: O(n)
        # Space Complexity: O(min(n, m)), where n is length of the string, m is number of unique characters
        
        left = 0
        max_length = 0

        # Dictionary to store the index of the characters
        character_index_map = {}
        
        # Iterate through string with right pointer
        for right in range(len(s)):
            # Character already in the window (i.e. substring)
            if s[right] in character_index_map and character_index_map[s[right]] >= left:
                # Move left pointer to the right of the previous occurrence of current character
                left = character_index_map[s[right]] + 1
            
            # Update or add current character's index to map
            character_index_map[s[right]] = right
            
            # Update maximum length of the substring found so far
            max_length = max(max_length, right - left + 1)
        
        return max_length
