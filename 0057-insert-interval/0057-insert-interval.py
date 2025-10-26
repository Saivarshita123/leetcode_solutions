class Solution:
    def insert(self, intervals, newInterval):
        res = []
        i = 0
        n = len(intervals)
        start, end = newInterval

        # Step 1: Add all intervals that come before newInterval
        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1

        # Step 2: Merge all overlapping intervals with newInterval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])

       
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
