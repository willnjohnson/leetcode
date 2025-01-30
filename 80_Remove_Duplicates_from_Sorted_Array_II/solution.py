class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1  # Start with the first element
        count = 1  # Keep track of count of current element
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1  # Reset count for new element
            
            if count <= 2:  # Ensure up to two occurrences of the current element
                nums[k] = nums[i]
                k += 1
        
        return k
