class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, i = [], 0
        
        # Add intervals that come before the new interval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # Merge all intervals that overlap with new interval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Add merged new interval
        res.append(newInterval)
        
        # Add remaining intervals after the new interval
        res.extend(intervals[i:])
        
        return res
