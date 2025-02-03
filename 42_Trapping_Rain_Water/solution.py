class Solution:
    def trap(self, height: List[int]) -> int:
        # No water can be trapped, so return 0
        if not height:
            return 0
        
        # Time complexity - O(n) since we iterate through array once with two (left and right) pointers
        # Space complexity - O(1) because amount of extra space for pointers and max values are constant

        # Initialize pointers and maximum heights
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        # Accumulate total amount of trapped water
        water_trapped = 0
        
        # Loop until pointers converge
        while left < right:
            if height[left] <= height[right]:
                if height[left] < left_max:
                    # Calculate the water trapped above current bar
                    water_trapped += left_max - height[left]
                else:
                    # Update left_max to current height since it's higher than the previous left_max
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    # Calculate the water trapped above current bar
                    water_trapped += right_max - height[right]
                else:
                    # Update right_max to current height since it's higher than the previous right_max
                    right_max = height[right]
                right -= 1
        
        return water_trapped
