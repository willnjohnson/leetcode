class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Note: if twoSum was sorted to begin with, we can use left and right pointer
        # and increment until we reach target, which can achieve less than O(N^2)

        # Since Example 2 isn't sorted, the best approach will be to use a hashmap
        # Time complexity is O(N) to iterate across n elements, with O(1) hash insertion and lookup

        map = {}
        for i, num in enumerate(nums):
            # Calculate complement
            comp = target - num

            # Check if complement exists in map (return if true)
            if comp in map:
                return [map[comp], i]
            
            # Store number
            map[num] = i
        
        return [-1]