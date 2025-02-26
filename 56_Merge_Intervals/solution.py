class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort based on starting interval
        intervals.sort(key=lambda x: x[0])
        merged = []
        
        for curr in intervals:
            if merged and curr[0] <= merged[-1][1]:
                # Current interval overlap, so merge by updating the end
                merged[-1][1] = max(merged[-1][1], curr[1])
            else:
                # No overlap, so add interval as is
                merged.append(curr)
        
        return merged
