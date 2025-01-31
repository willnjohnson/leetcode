class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # In case k is larger than the length of the array
        
        # [1] Reverse the entire array
        nums.reverse()
        
        # [2] Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        
        # [3] Reverse the remaining n-k elements
        nums[k:] = reversed(nums[k:])
