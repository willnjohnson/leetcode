class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)       # Total n elements
        result = [1] * n    # For n elements, set each element to 1
        
        # Step 1: Calculate the prefix product for each element
        # Example:
        #   Assume: nums:   [1, 2, 3, 4]
        #           result: [1, 1, 1, 1]
        #
        #   Updates to result:
        #     i=0: [1, 1, 1, 1] (prefix = 1)
        #     i=1: [1, 1, 1, 1] (prefix = 1*2 = 2)
        #     i=2: [1, 1, 2, 1] (prefix = 2*3 = 6)
        #     i=3: [1, 1, 2, 6] (prefix = 6*4 = 24)
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # Step 2: Calculate the suffix product for each element
        # Example:
        #   Assume: nums:   [1, 2, 3, 4]
        #           result: [1, 1, 2, 6]
        #
        #     i=3: [1, 1, 2, 6] (suffix = 1*4 = 4)
        #     i=2: [1, 1, 8, 6] (suffix = 4*3 = 12)
        #     i=1: [1, 12, 8, 6] (suffix = 12 * 2 = 24)
        #     i=0: [24, 12, 8, 6] (suffix= 24 * 1 = 24)
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result