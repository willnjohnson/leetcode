from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Strategy: Sliding Window + Hash Map / Frequency Count
        # Time Complexity: O(m + n), where m is the length of s, and n is the length of t
        # Space Complexity: O(n), where n is the number of unique characters in t
        
        if not s or not t:
            return ""
        
        # Frequency map of characters in t
        t_freq = Counter(t)
        required = len(t_freq)
        
        # Current window frequency map
        win_freq = Counter()
        
        left = min_left = formed = 0
        min_len = float('inf')
        
        # Iterate over the string s with right pointer
        for right in range(len(s)):
            char = s[right]
            win_freq[char] += 1
            
            # Check if the current window meets required frequency
            if win_freq[char] == t_freq[char]:
                formed += 1
            
            # If all characters from t are in the window, shrink
            while formed == required and left <= right:
                # Update result if current window smaller
                win_len = right - left + 1
                if win_len < min_len:
                    min_len = win_len
                    min_left = left
                
                # Shrink window from left
                win_freq[s[left]] -= 1
                if win_freq[s[left]] < t_freq[s[left]]:
                    formed -= 1
                left += 1
        
        # Return smallest window if found
        return s[min_left:min_left + min_len] if min_len != float('inf') else ""
