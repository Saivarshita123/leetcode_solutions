class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1       # Empty string has 1 valid decoding
        dp[1] = 1       # If first char is not '0', it has 1 decoding

        for i in range(2, n + 1):
            # Single-digit check
            if s[i-1] != '0':
                dp[i] += dp[i - 1]

            # Two-digit check
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
