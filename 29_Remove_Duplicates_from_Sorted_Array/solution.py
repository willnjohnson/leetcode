class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Assumes end of list
        if not nums:
            return 0
        
        # Pointer to place next unique element
        k = 1
        
        # Iterate through array starting from the element index 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        
        return k # Return number of unique elements
