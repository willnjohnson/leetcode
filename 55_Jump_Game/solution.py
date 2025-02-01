class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_index = 0
        
        for i in range(len(nums)):
            if i > farthest_index:  # If we're at an index that we can't reach, return False
                return False
            
            # Otherwise, update the farthest index we can reach
            farthest_index = max(farthest_index, i + nums[i])

            # If we can reach or if we exceed the last index, return True
            if farthest_index >= len(nums) - 1:
                return True
        
        return False 
