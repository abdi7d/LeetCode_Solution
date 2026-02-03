class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their end points
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        count = 0  # number of non-overlapping intervals found so far
        end = float('-inf') # end point of the last non-overlapping interval
        
        for interval in intervals:
            start_i, end_i = interval
            # If the current interval does not overlap with the previous one
            if start_i >= end:
                # Count it as a valid non-overlapping interval
                count += 1
                end = end_i
        
        # The total number of intervals is len(intervals)
        # The maximum number of non-overlapping intervals is 'count'
        # The number of intervals to remove is the difference
        return len(intervals) - count
