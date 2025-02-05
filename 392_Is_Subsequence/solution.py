class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # We can use two pointer technique
        i = 0 # corresponds to s
        j = 0 # corresponds to t

        # Make sure pointer doesn't exceed traversal
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move pointer in s
            j += 1  # Always move pointer in t
        return i == len(s)  # Evaluate traversing True, if all characters in s is traversed, else False