class Solution:
    def jump(self, nums: List[int]) -> int:
        # Set length n of list
        n = len(nums)

        # If list is length size 1, return 0 (for no jump)
        if n == 1: return 0
        
        # Otherwise, initialize variables
        jumps = 0
        curr_end = 0
        farthest_index = 0
        
        for i in range(n):
            # Update the farthest index we can reach from current position
            farthest_index = max(farthest_index, i + nums[i])
            
            # If we have reached the end of the current jump range
            if i == curr_end:
                # Do not update if the current jump range is GREATER THAN OR EQUAL TO n - 1
                if curr_end >= n - 1:
                    break

                # Otherwise in a normal case, update variables
                jumps += 1
                curr_end = farthest_index  # Move to the farthest reachable point
            
        return jumps
