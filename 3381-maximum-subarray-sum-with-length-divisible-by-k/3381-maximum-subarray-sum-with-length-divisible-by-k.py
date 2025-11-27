class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        INF = 10**30

        # min_prefix[i] = smallest prefix sum encountered at a prefix index with index % k == i
        min_prefix = [INF] * k
        min_prefix[0] = 0  # prefix sum at index 0 (before any element)

        prefix = 0
        ans = -INF

        # iterate prefix indices 1..n (prefix after adding nums[i-1])
        for i in range(1, n + 1):
            prefix += nums[i - 1]
            group = i % k                 # group by prefix index modulo k (important)
            # candidate: subarray that ends at index i-1 whose length is divisible by k
            ans = max(ans, prefix - min_prefix[group])
            # update smallest prefix sum for this group
            if prefix < min_prefix[group]:
                min_prefix[group] = prefix

        return ans
