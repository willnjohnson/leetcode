from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time complexity is O(n) as we count frequency of at most n characters in both sets then check if frequencies are equal to each other

        '''
        # Note, we can use unicodedata to normalize the strings to support Unicode characters

        s = unicodedata.normalize('NFC', s)
        t = unicodedata.normalize('NFC', t)
        '''

        return Counter(s) == Counter(t)
