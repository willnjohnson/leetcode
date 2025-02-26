class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        
        res = []
        start = nums[0]
        
        for i in range(1, len(nums) + 1):
            # As long as sequence isn't broken and list hasn't ended
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                # Either insert the range or a single number to res list
                if start == nums[i - 1]:    res.append(str(start))
                else:                       res.append(f"{start}->{nums[i - 1]}")

                # Update range
                if i < len(nums):           start = nums[i]
        
        return res
