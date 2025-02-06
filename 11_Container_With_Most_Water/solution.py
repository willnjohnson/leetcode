'''
O(N^2) technique:

While this solution works, it's not the BEST solution,
because we end up checking repeated elements in the list

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0

        for i in range(len(height)):
            for j in range(len(height)):
                if height[i] < height[j]:
                    t = height[i]*abs(j-i)
                    if maximum < t:
                        maximum = t

                else:
                    t = height[j]*abs(j-i)
                    if maximum < t:
                        maximum = t
        
        return maximum

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # We can use the two pointer approach to optimize the time complexity to O(N)
        # Set left pointer to start
        # Set right pointer to end
        #
        # Move the pointer with the shorter line inward until the pointers meet

        left = 0
        right = len(height) - 1
        maximum = 0

        while left < right:
            # Calculate area with current left and right lines
            area = (right - left) * min(height[left], height[right])
            maximum = max(maximum, area)
            
            # Move pointer at the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maximum
