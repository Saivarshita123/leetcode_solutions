class Solution:
    def maxTwoEvents(self, events):
        # Sort events by end time
        events.sort(key=lambda x: x[1])

        n = len(events)
        ends = [0] * n
        maxValue = [0] * n

        # Build ends[] and maxValue[]
        for i in range(n):
            ends[i] = events[i][1]
            maxValue[i] = events[i][2] if i == 0 else max(maxValue[i-1], events[i][2])

        ans = 0

        for i in range(n):
            start, end, value = events[i]
            ans = max(ans, value)  # Case: take only one event

            # Binary search for last event that ends < start
            left, right = 0, i - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if ends[mid] < start:
                    idx = mid
                    left = mid + 1
                else:
                    right = mid - 1

            if idx != -1:
                ans = max(ans, value + maxValue[idx])

        return ans
