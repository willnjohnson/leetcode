class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create frequency arrays for the ransomNote and magazine, which holds 26 letters (a-z)
        cnt_ransomNote = [0] * 26
        cnt_magazine = [0] * 26
        
        # Count frequencies of each character in ransomNote
        for char in ransomNote:
            cnt_ransomNote[ord(char) - ord('a')] += 1
        
        # Count frequencies of each character in magazine
        for char in magazine:
            cnt_magazine[ord(char) - ord('a')] += 1
        
        # Check if magazine has enough characters for ransomNote
        for i in range(26):
            if cnt_ransomNote[i] > cnt_magazine[i]:
                return False
        
        return True
