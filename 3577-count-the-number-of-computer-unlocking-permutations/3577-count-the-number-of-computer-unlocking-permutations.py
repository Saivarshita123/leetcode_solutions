class Solution:
    def countPermutations(self, complexity):
        MOD = 10**9 + 7
        n = len(complexity)
        # If any node i>0 has complexity <= complexity[0], it can never be unlocked.
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        # Otherwise, any ordering of the remaining n-1 computers works.
        ans = 1
        for i in range(1, n):   # multiply 1 * 2 * ... * (n-1)
            ans = (ans * i) % MOD
        return ans
