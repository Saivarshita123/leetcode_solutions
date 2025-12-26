class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Initial penalty: shop closes at hour 0
        penalty = customers.count('Y')
        min_penalty = penalty
        best_hour = 0

        # Traverse each hour
        for i, c in enumerate(customers):
            if c == 'Y':
                penalty -= 1   # one less Y in closed hours
            else:  # c == 'N'
                penalty += 1   # one more N in open hours

            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1  # shop closes after this hour

        return best_hour
