class Solution:
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # O(n) - We can use sliding window, maintain dynamic subarray
        #        where the sum is adjusted to be greater than or equal to target
        n = len(nums)
        left = 0
        total = 0
        min_len = float('inf')
        
        for right in range(n):
            total += nums[right]
            
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # O(n log n) - We can use binary search with prefix sum
        n = len(nums)
        left = 0
        total = 0
        min_len = float('inf')
        
        for right in range(n):
            total += nums[right]
            
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0