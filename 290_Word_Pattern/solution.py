class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Time complexity is O(n+m)
        # where n is number of words in s
        # and m is length of pattern

        words = s.split()
        if len(pattern) != len(words): return False
        return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))
