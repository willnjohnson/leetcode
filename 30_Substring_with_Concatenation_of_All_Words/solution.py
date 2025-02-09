from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Strategy: Sliding Window with Hash Map / Frequency Count
        # Time Complexity: O(n * m), where n is the length of string s, and m is the total length of all words combined
        # Space Complexity: O(k), where k is the number of unique words in the array

        if not s or not words:
            return []
        
        word_len = len(words[0])
        n_words = len(words)
        total_len = word_len * n_words
        word_freq = Counter(words)
        result = []
        
        # Iterate through each possible starting position in string
        for i in range(word_len):
            left = right = i
            curr_window_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]  # Get current word in the window
                right += word_len  # Move right pointer by length of one word
                
                if word in word_freq:
                    curr_window_count[word] += 1
                    
                    # If word count exceeds the number in words, shrink window
                    while curr_window_count[word] > word_freq[word]:
                        curr_window_count[s[left:left + word_len]] -= 1
                        left += word_len
                    
                    # If window contains all words, add start index to result
                    if right - left == total_len:
                        result.append(left)
                else:
                    # Reset window if word is not in words list
                    curr_window_count.clear()
                    left = right
        
        return result
