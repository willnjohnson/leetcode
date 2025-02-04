class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # In worse case, time complexity is O(N*M), where
        # N is number of strings in strs and
        # M is the length of the shortest string in the list

        # Space complexity is O(M), length of shortest string
        
        if not strs:
            return ""

        # Start with first string as prefix
        prefix = strs[0]

        for string in strs[1:]:
            # Update prefix, comparing it with each string
            while not string.startswith(prefix):
                # Decrease prefix
                prefix = prefix[:-1]

                # No common prefix
                if not prefix:
                    return ""
                    
        return prefix
