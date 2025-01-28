class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer to track the index of the next valid element
        
        # Iterate over the array
        for i in range(len(nums)):
            if nums[i] != val:
                # Place valid element at index k then increment k
                nums[k] = nums[i]
                k += 1
        
        return k  # Return number of valid elements
