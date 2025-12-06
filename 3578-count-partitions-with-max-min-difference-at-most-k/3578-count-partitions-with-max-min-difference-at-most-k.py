class Solution:
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)

        from collections import deque
        maxdq = deque()
        mindq = deque()

        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        dp[0] = prefix[0] = 1

        left = 0
        for right in range(n):
            # Update max deque
            while maxdq and nums[maxdq[-1]] <= nums[right]:
                maxdq.pop()
            maxdq.append(right)

            # Update min deque
            while mindq and nums[mindq[-1]] >= nums[right]:
                mindq.pop()
            mindq.append(right)

            # Shrink window from left until constraint satisfied
            while nums[maxdq[0]] - nums[mindq[0]] > k:
                left += 1
                if maxdq[0] < left:
                    maxdq.popleft()
                if mindq[0] < left:
                    mindq.popleft()

            # valid j range = [left .. right]
            # dp at index = sum(dp[left .. right])
            dp[right+1] = (prefix[right] - (prefix[left-1] if left > 0 else 0)) % MOD
            prefix[right+1] = (prefix[right] + dp[right+1]) % MOD

        return dp[n] % MOD
