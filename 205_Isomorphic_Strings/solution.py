class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        
        for i, j in zip(s, t):
            # Check if i is already mapped to different j
            if i in d and d[i] != j:
                return False
            
            # Check if j is already mapped in different i
            if i not in d and j in d.values():
                return False
            
            # Map character keyed at i to value j
            d[i] = j
        
        return True
