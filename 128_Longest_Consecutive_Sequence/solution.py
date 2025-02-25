class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums) # build set takes O(n) time but O(1) lookup
        longest = 0
        
        # Overall complexity is O(n), for looping through set and checking numbers
        for num in num_set:
            if num - 1 not in num_set:
                streak = 1
                while num + streak in num_set:
                    streak += 1
                longest = max(longest, streak)
        
        return longest