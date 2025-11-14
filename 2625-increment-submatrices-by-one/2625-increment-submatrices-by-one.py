class Solution:
    def rangeAddQueries(self, n: int, queries):
        # Step 1: Create a difference matrix
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # Step 2: For each query apply difference increments
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Step 3: Prefix sum row-wise
        for i in range(n):
            for j in range(1, n):
                diff[i][j] += diff[i][j - 1]

        # Step 4: Prefix sum column-wise
        for j in range(n):
            for i in range(1, n):
                diff[i][j] += diff[i - 1][j]

        # Step 5: Final matrix (cut to n×n)
        result = [[diff[i][j] for j in range(n)] for i in range(n)]
        return result
