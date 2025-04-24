class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Can use double-ended queue for efficient access to both ends

        dq, res = deque(), []

        for i, num in enumerate(nums):
            if dq and dq[0] <= (i - k):
                dq.popleft()
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res