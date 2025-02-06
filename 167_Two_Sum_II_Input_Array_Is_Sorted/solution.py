class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time complexity O(n): List traversal only occurs once
        # Use two-pointer technique with left at beginning and right at end of sorted list
        # Move pointers toward each other until there's a pair whose sum equals the target
        
        # Space complexity O(1):
        # Two pointers in use with constant number of variables

        left = 0
        right = len(numbers)-1
        
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1] # Return the 1-indexed positions
            elif curr_sum < target:
                left += 1 # Left pointer moves right
            else:
                right -= 1 # Right pointer moves left
