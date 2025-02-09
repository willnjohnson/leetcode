class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Strategy:
        # Sort the list to make it easier to avoid duplicate entries
        # Use two pointer technique

        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                # Calculate the sum of the three elements
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # Append valid triplet to result
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move the left pointer to the right, avoiding duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Move the right pointer to the left, avoiding duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers after processing valid triplet
                    left += 1
                    right -= 1
                elif total < 0:
                    # Increment left (to larger sum), if sum is larger than 0
                    left += 1
                else:
                    # Decrement right (to smaller sum), if sum is greater than or equal to 0
                    right -= 1
        
        return result
