from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # Base profit
        base_profit = sum(strategy[i] * prices[i] for i in range(n))

        # Prefix sums
        pref_strat = [0] * (n + 1)
        pref_price = [0] * (n + 1)

        for i in range(n):
            pref_strat[i + 1] = pref_strat[i] + strategy[i] * prices[i]
            pref_price[i + 1] = pref_price[i] + prices[i]

        half = k // 2
        max_delta = 0

        for l in range(n - k + 1):
            r = l + k

            # Old contribution in this window
            old_profit = pref_strat[r] - pref_strat[l]

            # New contribution: second half becomes sell (1)
            new_profit = pref_price[r] - pref_price[l + half]

            delta = new_profit - old_profit
            max_delta = max(max_delta, delta)

        return base_profit + max_delta
