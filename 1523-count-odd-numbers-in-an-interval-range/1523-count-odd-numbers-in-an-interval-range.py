class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Count how many odd numbers are ≤ high
        odds_up_to_high = (high + 1) // 2
        
        # Count how many odd numbers are < low
        odds_before_low = low // 2
        
        # Difference gives count of odds in [low, high]
        return odds_up_to_high - odds_before_low
