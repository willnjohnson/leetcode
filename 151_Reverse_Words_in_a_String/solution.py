class Solution: 
    def reverseWords(self, s: str) -> str:
        # Note in Python: strings are immutable, so
        # trying to achieve O(1) space complexity is unreasonable

        # O(N) time and O(N) space complexity solution

        # Split string into words by using split() method
        words = s.split()
        
        # Reverse the list of words
        words.reverse()
        
        # Join the words back together with a single space
        return ' '.join(words)