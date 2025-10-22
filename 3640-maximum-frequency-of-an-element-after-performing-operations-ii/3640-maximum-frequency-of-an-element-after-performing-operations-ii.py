from bisect import bisect_left, bisect_right
from collections import Counter

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        n = len(nums)
        if n == 0:
            return 0
        nums.sort()
        counts = Counter(nums)

        # 1) For each existing value v (we iterate by index i),
        # compute within_count = number of elements in [v-k, v+k]
        best_existing_target = 1
        for i, v in enumerate(nums):
            left = bisect_left(nums, v - k)
            right = bisect_right(nums, v + k)  # exclusive
            within_count = right - left
            freq_v = counts[v]
            candidate = min(freq_v + numOperations, within_count)
            if candidate > best_existing_target:
                best_existing_target = candidate

        # 2) Calculate window_max: max number of elements whose intervals intersect
        # i.e., max window with nums[r] - nums[l] <= 2*k
        l = 0
        window_max = 1
        for r in range(n):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            window_size = r - l + 1
            if window_size > window_max:
                window_max = window_size

        # 3) You can choose up to numOperations elements from such an overlapping window
        # and modify them all to a new value (not necessarily present initially).
        best_modify_only = min(window_max, numOperations)

        return max(best_existing_target, best_modify_only)
