class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        stored = {}

        for i, num in enumerate(nums):
            # Check conditions
            if num in stored and i - stored[num] <= k:
                return True
            
            stored[num] = i

        # Enumerated without finding such pair
        return False